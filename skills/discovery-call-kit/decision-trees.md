# Decision Trees: Discovery Call Kit

Run these in order. Every tree ends at a named exit; record the exit in the scorecard.

## Tree 1: Qualification verdict

```
START: Extraction complete, scores assigned (Fit / Budget / Timing / Access, each 0-3)
|
|-- Is there a category conflict with a current client?
|     YES -> EXIT D: DECLINE POLITELY (conflict). Say so on the next contact,
|            warmly, and offer to stay in touch if the conflict clears.
|     NO  -> continue
|
|-- Is Fit 0 (no provable match, or the work is work the studio does badly)?
|     YES -> EXIT D: DECLINE POLITELY (fit). A misfit engagement costs more
|            than an empty pipeline slot.
|     NO  -> continue
|
|-- Is the buying process extractive (concepts required pre-contract,
|   many studios, no budget conversation permitted)?
|     YES -> Offer the paid discovery route ONCE, positioned as the
|            evaluation mechanism.
|            |-- Buyer accepts the route -> EXIT B: PAID DISCOVERY FIRST
|            |-- Buyer refuses -> EXIT D: DECLINE POLITELY (process)
|     NO  -> continue
|
|-- Total score:
|     9-12, no dimension at 0, and Budget and Access each at 2 or more -> EXIT A: PURSUE TO PROPOSAL.
|            Hand the brief to the Scope and Pricing Architect.
|     6-8, or Budget/Access at 1 -> EXIT B: PAID DISCOVERY FIRST.
|            Price the learning, resolve the unknown, then propose.
|     4-5, Timing at 0-1 with real fit -> EXIT C: NURTURE.
|            Named trigger to watch, review date in the signal log.
|     0-3 -> EXIT D: DECLINE POLITELY.
|
OVERRIDE RULE: The seller may move a verdict one step (never from EXIT D on
conflict). The reason goes in the brief, in words. "Good feeling" is not a reason.
```

## Tree 2: Budget unknown handling

```
START: The call ended with budget shape unresolved.
|
|-- WHY is it unknown?
|
|-- Buyer genuinely does not know yet (project not costed internally)
|     -> Use history on the next contact: "What did [comparable project] cost?"
|        Still unknown -> Budget scores 1. Route via Tree 1; a paid discovery
|        with a stated fee is how the number gets real. Never fill the gap
|        with a market "typical" figure in the brief. Mark [NOT STATED].
|
|-- Buyer knows but will not say (benchmarking or negotiation posture)
|     -> Give structure, not numbers: phases, drivers, what moves cost up/down.
|        Propose the proposal with a defined scope and let the price sit inside
|        it. Budget scores 1, Access note records the posture honestly.
|
|-- Buyer says there is no budget (unfunded aspiration)
|     -> Ask what would have to happen for money to exist (event, approval,
|        next financial year). That answer sets the nurture trigger.
|        Budget scores 0-1. Tree 1 will route to nurture or discovery priced
|        small enough to be findable money.
|
|-- Seller gave a number live on the call (ballpark escape)
|     -> Record it in the brief AS SELLER TALK, flag it, and deal with it in
|        the follow-up email: re-anchor to scope ("the number I mentioned
|        assumed X deliverables; the scoped proposal will price what we
|        actually listed"). Do not let it harden into a ceiling unexamined.
|
EXIT: Budget has a score, the brief states the shape in the buyer's own words
or reads [NOT STATED], and one named action exists to resolve it.
```

## Tree 3: Wrong person on the call

```
START: It becomes clear the attendee cannot judge the work, does not control
budget, and cannot describe the decision process.
|
|-- Is this person a genuine user of the work (will live with the output)?
|     YES -> Run a USER discovery: needs, workflow, pain, production reality.
|            Do not ask them budget questions they cannot answer; mark Budget
|            and Access as they are. Close by asking for the route:
|            "Who owns this project commercially, and would you introduce us?"
|            EXIT: partial brief (creative/production fields strong, commercial
|            fields [NOT STATED]), Access scores 1, next step = sponsor call.
|
|-- Is this person a gatekeeper screening studios (procurement or assistant)?
|     YES -> Switch to the process agenda: criteria, weightings, panel or
|            onboarding steps, named business sponsor. Do not pitch creative.
|            EXIT: process map extracted, sponsor identification is the next
|            step, verdict cannot exceed Paid Discovery until the sponsor is met.
|
|-- Is this person a stand-in with no knowledge of the project at all?
|     YES -> Shorten gracefully. Extract whatever is real, thank them, and
|            rebook with the right person while goodwill is fresh. Record
|            almost nothing as stated: a stand-in's guesses are [NOT STATED]
|            with their name attached nowhere near a fact.
|            EXIT: rebooked call is the only deliverable.
|
EXIT: The brief never pretends the call reached the buying centre. Access is
scored on who was actually in the room.
```

## Tree 4: Timeline impossible, options

```
START: The back-calculation (shelf or launch date minus distribution, print,
artwork lock) shows the stated deadline cannot carry the stated scope.
|
|-- Step 1: Verify the chain on the call, out loud, kindly.
|   "Shelf date is X. Print needs Y weeks, artwork lock is Z. Full scope
|    lands two weeks past Z. Let us look at the levers together."
|
|-- Lever 1: SCOPE. Split the launch: hero SKUs or lead market on the date,
|   the remainder in phase 2. Feasible?
|     YES -> EXIT: phased proposal. Brief records the split explicitly.
|
|-- Lever 2: SEQUENCE. Start before full approval where the client can
|   (a letter of intent, strategy starts while artwork waits on sign-off).
|     YES -> EXIT: proposal with a stated conditional start and its risks.
|
|-- Lever 3: MONEY. Rush is real: parallel teams, out-of-hours, compressed
|   rounds. It is priced as rush through the studio's multiplier, agreed
|   before work starts, never absorbed silently.
|     YES -> EXIT: proposal with the rush line visible.
|
|-- No lever accepted, date treated as immovable, scope unchanged?
|     -> EXIT: DECLINE THE DATE, not the client. "We cannot sign up to a
|        date the physics does not allow; if the date moves or the scope
|        splits, we are in." A studio that accepts impossible dates buys
|        itself a failure it will be remembered for.
|
EXIT: The brief's timeline field always shows the back-calculation, not just
the date the buyer wished for.
```
