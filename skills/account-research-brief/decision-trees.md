# Decision Trees: Account Research Brief

Run these trees in order after the signals sweep. Each tree ends in a defined exit. Do not override an exit silently: if you override, write the reason in the brief.

## Tree 1: Signal strength

```
START: What did the sweep find?
|
|-- IF there are 2+ confirmed signals forming a stack (see playbook)
|   that points at the same work in the same window
|   THEN strength = STRONG
|   -> EXIT: Continue to Tree 2 with pursue-now as the default outcome.
|
|-- IF there is exactly 1 confirmed signal, OR 2+ signals that
|   do not point at the same work
|   THEN strength = MODERATE
|   -> Continue to Tree 2. Default outcome is watchlist unless
|      Trees 2 and 3 both come out at their best exits.
|
|-- IF the only signals are reported (single credible source)
|   or unverified
|   THEN strength = WEAK
|   -> EXIT: WATCHLIST. Record the verification step that would
|      upgrade the signal. Do not brief for outreach.
|
|-- IF there are no dated signals at all
|   THEN strength = NONE
|   -> EXIT: DO NOT PURSUE. File the brief with the sweep record
|      and a review date two quarters out.
|
|-- IF signals exist but all are older than 6 months with no
    newer signal reactivating them
    THEN strength = STALE (treat as NONE)
    -> EXIT: DO NOT PURSUE for now. Keep the stale signals in the
       log as context and set a 90-day review.
```

## Tree 2: Portfolio match

```
START: Score portfolio match from the studio fact sheet (0 to 3).
|
|-- IF match = 3 (same deliverable, same or adjacent category,
|   named proof the studio can show)
|   THEN -> Continue to Tree 3. No discount on the hypothesis.
|
|-- IF match = 2 (same deliverable, new category, OR same category,
|   adjacent deliverable)
|   THEN -> Continue to Tree 3. The brief must name the gap plainly
|   and the hypothesis confidence caps at MEDIUM.
|
|-- IF match = 1 (plausible capability, nothing to show)
|   THEN -> EXIT: WATCHLIST, unless the user confirms this is a
|   deliberate category-entry play AND deal size scores 3.
|   In that case continue to Tree 3 with confidence capped at LOW
|   and the entry-play reasoning written in the brief.
|
|-- IF match = 0 (outside services, excluded category, or an
    active conflict with a current client in the same category)
    THEN -> EXIT: DO NOT PURSUE. Signal strength is irrelevant.
    Record the conflict or capability gap as the reason.
```

## Tree 3: Timing

```
START: Place the buying window using the signal dates and the
windows in the playbook taxonomy (and, for packaging, the retailer
reset calendar).
|
|-- IF the window is open now (key signal dated within the last
|   quarter, deadline or launch still ahead)
|   THEN timing = NOW
|   -> EXIT: PURSUE NOW if Trees 1 and 2 allowed it. First action
|      within 2 weeks. Brief review date: 30 days.
|
|-- IF the window opens within the next 1 to 2 quarters (dated
|   future trigger: a reset, a launch, a leader's first 90 days
|   still to run)
|   THEN timing = THIS QUARTER / NEXT
|   -> EXIT: WATCHLIST with the trigger named and a review date
|      2 to 4 weeks before the window opens, OR pursue now with a
|      relationship-opening angle if portfolio match = 3.
|
|-- IF the window is seasonal and recurring (fashion seasons,
|   holiday ranges, annual resets) but the current cycle is closed
|   THEN timing = SEASONAL
|   -> EXIT: WATCHLIST. Review date set to the start of the next
|      buying cycle for that season, not a generic 90 days.
|
|-- IF the window has already closed (product in market with
|   finished design, roster already announced, leader past 180
|   days with a set roster)
|   THEN timing = CLOSED
|   -> EXIT: DO NOT PURSUE this cycle. Log the signals that will
|      define the next cycle and set the review to that horizon.
|
|-- IF no window can be placed from dated evidence
    THEN timing = UNKNOWN
    -> EXIT: WATCHLIST at best. Record what fact would place the
       window. Unknown timing plus weak signals = DO NOT PURSUE.
```

## Tree 4: Buyer identified or unknown

```
START: Can the brief name the likely buying centre from sources?
|
|-- IF a named brand-side owner is identified (brand director,
|   head of brand, founder) with source and date, and they are
|   plausibly in the buying window (see new-leader signal)
|   THEN buyer = IDENTIFIED (BRAND)
|   -> EXIT: Brief routes to outreach planning aimed at that role.
|      Note tenure and background in the stakeholder map.
|
|-- IF the account is known to buy through procurement (roster,
|   panel, tender, group-mandated agency list)
|   THEN buyer = IDENTIFIED (PROCUREMENT-LED)
|   -> EXIT: Brief must state the process reality and the cost of
|      playing (onboarding, rate card, tender effort). Recommendation
|      is PURSUE only if the studio already plays procurement-led
|      accounts per the fact sheet; otherwise WATCHLIST pending a
|      brand-side sponsor appearing.
|
|-- IF the brand is founder-led and no professional brand lead
|   exists
|   THEN buyer = IDENTIFIED (FOUNDER)
|   -> EXIT: Brief notes taste-led buying: fast decisions, proof
|      and conviction matter more than process. Route to outreach
|      planning with a founder-appropriate angle.
|
|-- IF no owner can be identified from any source
|   THEN buyer = UNKNOWN
|   -> EXIT: The brief cannot recommend PURSUE NOW on its own.
|      Downgrade one level (pursue becomes watchlist, watchlist
|      stays watchlist) and record "identify the buying centre"
|      as the first research action for the review date.
|
|-- IF the named owner has left, or the role is vacant or interim
    THEN buyer = IN TRANSITION
    -> EXIT: WATCHLIST. A vacant or interim seat freezes most
       buying. Review when the permanent appointment is announced;
       that announcement is itself a Tree 1 signal.
```
