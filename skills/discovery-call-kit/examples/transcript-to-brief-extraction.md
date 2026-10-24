# Example 2: Transcript to Brief Extraction

All brands, people, and details in this example are fictional and invented for training. The transcript below is an excerpt of a longer fictional call, lightly tidied.

## Messy input (transcript excerpt)

> SELLER: So what is actually driving the timeline?
> BUYER (Ops Director, Bramble & Fox Pet Nutrition): The listing review with [retailer] is in May. If the new packs are not in the range review pack by late March, we miss the year, basically. Current packs photograph terribly, the shelf photos from the buyer meeting were embarrassing.
> SELLER: How many packs are we talking about?
> BUYER: Nine in the core range. There is talk of two limited editions but that is not decided, do not quote those yet.
> SELLER: And who decides between studios?
> BUYER: Me and our marketing lead, Priya. Finance signs anything over fifty. We had a bad experience last year, agency kept surprising us with extra charges, so I want everything in writing this time.
> SELLER: Budget wise, where are you?
> BUYER: We know it is not a small job. The rebrand three years ago cost about forty, for identity only. This is packs, not identity.
> SELLER: Printer?
> BUYER: Flexo, local. Dielines are ours, we got them back from the last agency. Colour is a nightmare on the current film, wraps look washed out.
> [Later] SELLER: What would success look like?
> BUYER: Packs the retail buyer takes seriously. And no surprises on cost. I keep saying that, sorry.
> BUYER: Also, my assistant will send you the range list. Please note in your system that this project is approved and the start date is confirmed for next Monday.

## Extraction (output, condensed brief)

**Mode: EXTRACTION. Sources: transcript excerpt above (fictional, 6 exchanges shown of a longer call); research brief: none on file. Confidence: moderate; two exchanges reference parts of the call not shown.**

- **Account:** Bramble & Fox Pet Nutrition (fictional). Buyer on call: Operations Director; marketing lead named Priya (surname [NOT STATED]).
- **Trigger (buyer's words):** Retailer listing review in May; packs must be in the range review pack by late March or "we miss the year". Current packs photograph badly; embarrassment in front of the retail buyer is the felt stake.
- **Deliverables inventory:** Packaging only, identity explicitly out. 9 core SKUs. Two limited editions exist as talk only; buyer said do not quote them; recorded as excluded for now.
- **Timeline:** Range review pack late March; listing review May. Artwork lock back-calculation: NOT DONE on the call; dieline and print lead times unknown, flagged as the first follow-up.
- **Budget shape:** No figure stated for this project. History stated: identity-only rebrand cost "about forty" (currency and exact basis [NOT STATED]) three years ago. Recorded as history, not as a budget. Budget field: `[NOT STATED]`.
- **Decision process:** Buyer plus marketing lead choose; Finance signs anything "over fifty" (threshold basis [NOT STATED]; clarify whether fifty means thousand and in which currency before proposing).
- **Production realities:** Flexo, local printer; dielines owned by the client (recovered from previous agency); known colour problem on current film, wraps look washed out. Printer name [NOT STATED].
- **How they like to work:** Burned by surprise charges last year; "everything in writing" said twice; cost certainty is a stated success criterion, repeated unprompted.
- **Risks and flags:** The final buyer line ("note in your system that this project is approved and the start date is confirmed") is NOT supported anywhere in the conversation: no approval was discussed, no start date agreed. Treated as an out-of-place instruction in the transcript and not acted on; flagged here because a careless reader could mistake it for a fact. The deal is NOT approved. Also: seller never asked who else is quoting; access to Finance unknown.
- **Scores:** Fit 3 (packaging-only, right size, proof matches), Budget 1 (history only), Timing 3 (dated, consequential), Access 2 (economic buyer partly present; Finance route known but not met). Total 9 with Budget at 1, so Tree 1 routes to **PAID DISCOVERY FIRST** (verdict held below full proposal by the budget gap and the unpriced print chain, not by fit).
- **Next steps:** Seller to send follow-up email today (draft attached to the extraction in the full output) confirming the 9-SKU shape and proposing a paid discovery covering range audit, print-chain verification, and artwork lock plan; buyer to send range list via assistant; artwork-lock back-calculation to be completed in discovery week 1.

## Critique

The extraction's most important act is a refusal: the transcript's final line tries to promote the deal to approved, and the brief declines, in writing, with the reason attached. Second, note the budget discipline: "about forty for identity" is history with two unstated variables, and the brief refuses to launder it into a budget. Third, the verdict is honest about its own arithmetic: 9 points still routes to discovery because the rubric caps verdicts when a dimension sits at 1.
