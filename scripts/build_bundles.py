#!/usr/bin/env python3
"""Build release ZIPs for the Creative Sales Suite and run the repo checks.

Usage: python3 scripts/build_bundles.py --version 1.1.0 [--out dist]

Outputs (in the out dir):
  creative-sales-suite-full.zip    the whole suite (no website, no scripts, no .git)
  <skill>-core.zip                 one skill's tested core set (10 files) + fact sheet template
  <skill>-full.zip                 one skill's complete folder
  claude-skill-<skill>.zip         one skill folder, ready for Claude Skills upload

Checks run first and fail the build: SKILL.md frontmatter (name matches the
folder, description present and under 1024 characters) and internal markdown
links across the repo.
"""
import argparse, pathlib, re, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
CORE_TOP = ["SKILL.md", "playbook.md", "decision-trees.md", "self-check.md"]

def check_frontmatter():
    errors = []
    for skill_md in sorted(ROOT.glob("skills/*/SKILL.md")):
        folder = skill_md.parent.name
        text = skill_md.read_text()
        if not text.startswith("---\n"):
            errors.append(f"{folder}: SKILL.md has no frontmatter"); continue
        fm = text.split("---\n", 2)[1]
        name = re.search(r"^name:\s*(.+)$", fm, re.M)
        desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not name or name.group(1).strip() != folder:
            errors.append(f"{folder}: frontmatter name does not match folder")
        if not desc:
            errors.append(f"{folder}: frontmatter description missing")
        elif len(desc.group(1).strip()) > 1024:
            errors.append(f"{folder}: description over 1024 characters")
    return errors

def check_links():
    errors = []
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts or "dist" in md.parts:
            continue
        for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", md.read_text(errors="ignore")):
            url = m.group(1).split("#")[0].strip()
            if not url or url.startswith(("http://", "https://", "mailto:")):
                continue
            if not (md.parent / url).exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link {url}")
    return errors

def add_tree(zf, folder, arc_prefix, skip_parts=()):
    for f in sorted(folder.rglob("*")):
        if f.is_file() and not any(p in f.parts for p in skip_parts):
            zf.write(f, pathlib.Path(arc_prefix) / f.relative_to(folder))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", required=True)
    ap.add_argument("--out", default="dist")
    args = ap.parse_args()
    errors = check_frontmatter() + check_links()
    if errors:
        print("CHECKS FAILED:"); [print(" -", e) for e in errors]; sys.exit(1)
    print("checks passed: frontmatter ok, internal links ok")
    out = ROOT / args.out; out.mkdir(exist_ok=True)
    build_info = f"Creative Sales Suite v{args.version}\nBuilt by scripts/build_bundles.py\nLicense: MIT\n"
    # full suite
    with zipfile.ZipFile(out / "creative-sales-suite-full.zip", "w", zipfile.ZIP_DEFLATED) as zf:
        for item in sorted(ROOT.iterdir()):
            if item.name in {".git", "dist", "docs", "scripts"}: continue
            if item.is_dir(): add_tree(zf, item, item.name)
            elif item.is_file(): zf.write(item, item.name)
        zf.writestr("BUILD-INFO.txt", build_info)
    # per-skill zips
    for skill in sorted((ROOT / "skills").iterdir()):
        core_files = [skill / f for f in CORE_TOP] + sorted((skill / "templates").glob("*.md"))
        with zipfile.ZipFile(out / f"{skill.name}-core.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            for f in core_files: zf.write(f, pathlib.Path(skill.name) / f.name if f.parent == skill else pathlib.Path(skill.name, "templates") / f.name)
            zf.write(ROOT / "start-here/fact-sheet-template.md", "start-here/fact-sheet-template.md")
            zf.writestr("BUILD-INFO.txt", build_info)
        with zipfile.ZipFile(out / f"{skill.name}-full.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            add_tree(zf, skill, skill.name)
        with zipfile.ZipFile(out / f"claude-skill-{skill.name}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            add_tree(zf, skill, skill.name)
    for z in sorted(out.glob("*.zip")):
        print("built", z.name, f"{z.stat().st_size//1024} KB")
if __name__ == "__main__":
    main()
