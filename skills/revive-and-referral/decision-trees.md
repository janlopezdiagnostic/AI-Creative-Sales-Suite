# Decision Trees: Revive and Referral

Run Tree 4 first, always. Then Tree 1 and Tree 2 for revival work, Tree 3 for referral asks. Each tree ends in a defined exit. Do not override an exit silently: if you override, write the reason in the tracker.

## Tree 4: Contact permission check (run before anything else)

```
START: Is this contact/account clear to contact?
|
|-- IF the contact ever asked not to be contacted, unsubscribed,
|   or said words to that effect in any channel
|   THEN permission = NONE. PERMANENT.
|   -> EXIT: STOP. No revival, no breakup email, no referral ask,
|      ever. Record "do not contact" and the source of the request.
|
|-- IF the account or contact is marked do-not-contact in the CRM,
|   OR a colleague recorded an opt-out the user cannot evidence away
|   THEN permission = NONE until proven otherwise.
|   -> EXIT: STOP. Treat as an opt-out. The burden of proof sits
|      with contacting, not with silence.
|
|-- IF the client ended the relationship itself, or the loss was a
|   genuine conflict (category conflict, conduct rupture)
|   THEN permission = CLOSED ACCOUNT.
|   -> EXIT: STOP. File as closed, not stalled. No engine runs.
|
|-- IF the last outcome was a clear stated "no" to the proposal
|   (not silence: an actual no, with or without a reason)
|   THEN permission = CLOSED unless a strong new trigger fires AND
|   the no was about timing, budget, or scope (not about the studio)
|   -> EXIT: Park in tracker. Revival only via Tree 2 with a
|      confirmed trigger, and the touch must acknowledge the no.
|
|-- OTHERWISE (silence, stall, soft deferral, no negative record)
    THEN permission = CLEAR.
    -> Continue to Tree 1 (revival) or Tree 3 (referral).
```

## Tree 1: Stall cause to revival play

```
START: Permission is CLEAR (Tree 4). What is the primary stall cause
(from the deal history, see playbook Part 1)?
|
|-- NO DECISION (proposal sent, warmth, then silence)
|   |
|   |-- IF a trigger has fired (Tree 2 says ACT)
|   |   -> PLAY: Value-add touch built on the trigger.
|   |-- IF two touches have gone unanswered with no new trigger
|   |   -> PLAY: One breakup email, then park or close per reply.
|   |-- OTHERWISE -> PLAY: Park with named trigger watch + review date.
|
|-- LOST TO INCUMBENT (a decision was made, not for you)
|   |
|   |-- IF the scope in play is work the incumbent does not cover,
|   |   OR visible incumbent failure/capacity strain is sourced+dated
|   |   -> PLAY: Narrow-scope touch on the uncovered work only.
|   |-- OTHERWISE -> PLAY: Long game. Gracious close (if not already
|      sent), tracker entry, quarterly value-add at most, roster-review
|      and leadership-change triggers on watch.
|
|-- BUDGET FROZEN (client stated a money reason, often with a date)
|   |
|   |-- IF the named budget cycle window is within 30 days
|   |   -> PLAY: Budget-cycle return: original scope re-cut to the
|   |      known budget reality, sent just before planning opens.
|   |-- OTHERWISE -> PLAY: Park until 30 days before that window.
|      No interim check-ins that contradict the date they gave you.
|
|-- CHAMPION GONE (sponsor left or lost influence)
|   |
|   |-- IF a successor is named in a sourced announcement
|   |   -> PLAY: New-champion introduction: concise history of the
|   |      stalled work, zero blame, proposal attached as history.
|   |-- IF the champion resurfaced at a new company (sourced)
|   |   -> PLAY: Treat as a NEW account: conflict check, Skill 1
|   |      brief first, warm-path outreach. Not a continuation.
|   |-- OTHERWISE -> PLAY: Park. Watch for successor news.
|
|-- TIMING WRONG (client named a calendar/contract reason)
    |
    |-- IF the named window opens within 30 days
    |   -> PLAY: Return touch referencing exactly what they said
    |      and when, with the relevant seasonal/reset maths done.
    |-- OTHERWISE -> PLAY: Park until 30 days before the window.
       At most one strong-trigger touch in the interval.
```

## Tree 2: Trigger strength to act, watch, or drop

```
START: A candidate trigger for a parked or stalled deal.
|
|-- IF the trigger is confirmed (primary source or two independent
|   sources), dated within the last 90 days, AND it directly changes
|   the original blocking condition (budget, champion, timing, need)
|   THEN strength = ACT
|   -> EXIT: Build the revival touch now. One touch, built on this
|      trigger. Log the trigger, source, and date in the tracker.
|
|-- IF the trigger is reported (one credible source) and relevant,
|   OR confirmed but only loosely connected to the blocking condition
|   THEN strength = WATCH
|   -> EXIT: No touch yet. Raise the account's review frequency,
|      name the corroboration or follow-on event that would upgrade
|      it to ACT, set a review date within 30 days.
|
|-- IF the trigger is unverified, undated, older than 6 months with
|   no fresher corroboration, OR irrelevant to why the deal stalled
|   THEN strength = DROP
|   -> EXIT: Discard as a revival basis. Record it in the tracker
|      as checked and rejected, with the reason, so it is not
|      rediscovered and re-litigated next quarter.
|
|-- IF the "trigger" is bad news for the client (recall, scandal,
|   layoffs, public crisis) with no legitimate service angle
|   THEN strength = DO NOT USE
|   -> EXIT: No touch. Note the event, move any planned contact to
|      after the situation resolves, if it remains appropriate at all.
```

## Tree 3: Referral timing to ask, wait, or never

```
START: A client (current or past) is a candidate for an ask.
Evidence first: what satisfaction evidence exists, and how fresh?
|
|-- IF there is NO concrete evidence (no client words, no outcome,
|   no repeat purchase), OR the only evidence is older than a year,
|   OR a later problem postdates the praise and is unresolved
|   THEN verdict = NEVER (for now)
|   -> EXIT: No ask. Record what evidence would change this.
|
|-- IF there is an open complaint, live delivery problem, budget
|   dispute, or overdue-invoice tension with this client
|   THEN verdict = NEVER (until resolved and a fresh peak occurs)
|   -> EXIT: No ask. Fix the delivery issue. Note in the log.
|
|-- IF an ask was made to this client within the last two quarters
|   (any outcome, including ignored)
|   THEN verdict = WAIT
|   -> EXIT: No ask. Next eligibility: a new satisfaction peak at
|      least two quarters after the last ask.
|
|-- IF a satisfaction peak is live now (launch within ~3 weeks,
|   results shared by the client, unsolicited praise on record,
|   repeat project just kicked off, rescue confirmed good)
|   THEN verdict = ASK NOW
|   -> EXIT: One ask, matched to the evidence strength (playbook
|      Part 6 ladder: review < testimonial < case study < intro).
|      Draft with the effortlessness kit. Log the ask.
|
|-- IF evidence is solid but no peak is live (project delivered
|   well 2-6 months ago, no recent moment)
|   THEN verdict = WAIT for a named peak
|   -> EXIT: No generic ask. Log the expected peak (launch date,
|      results review, seasonal moment) and review then.
|
|-- IF the proposed ask includes any personal incentive, gift, or
    benefit to the client that their employer has not sanctioned
    THEN verdict = NEVER
    -> EXIT: Strip the incentive. If the ask only works with it,
       the ask does not happen.
```
