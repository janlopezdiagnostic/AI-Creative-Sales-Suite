# Decision Trees: Portfolio-Matched Outreach

Run these trees in order before and during outreach. Each tree ends in a defined exit. Do not override an exit silently: if you override, write the reason in the draft set and flag it to the human reviewer.

## Tree 1: Match strength

```
START: Score every plausible case-study library entry on the six
relevance axes in playbook.md (category proximity, format and
deliverable match, buyer-type match, outcome relevance, recency,
proof asset quality), each 0 to 3. Total is out of 18.
|
|-- IF total = 14 to 18 AND no axis = 0 AND category proximity
|   >= 2 AND format match >= 2 AND outcome relevance >= 2
|   THEN grade = STRONG
|   -> EXIT: SEND FULL MATCHED OPENER. One primary case study,
|      strongest claim the library supports at its permission
|      level, specific ask per the opener anatomy. Keep the
|      backup entry for a follow-up or a reply.
|
|-- IF total = 9 to 13, OR total >= 14 but one Strong minimum
|   is missed, AND category proximity >= 1 AND format match
|   >= 1 AND the entry is not internal only, never cite
|   THEN grade = PARTIAL
|   -> EXIT: SEND OBSERVATION-LED OPENER WITH SOFTENED PROOF.
|      Trigger and observation lead. Proof is capability
|      framing only: kind of work and category context, no
|      stretched claims, no figures or results beyond what the
|      library plainly supports, naming only at permission
|      level. Record the gap in the draft set.
|
|-- IF category proximity = 0 OR format match = 0 for every
|   plausible entry
|   THEN grade = NONE for that entry set
|   -> EXIT: DO NOT SEND generic outreach. See the NONE exit
|      below. A high total on other axes does not fix proof
|      about different work in a different category.
|
|-- IF total <= 8, OR every plausible entry is internal only,
    never cite, OR no complete library entry exists
    THEN grade = NONE
    -> EXIT: DO NOT SEND generic outreach. Options only:
       (a) wait for a better trigger and return the account to
       the watchlist with the trigger and review date named;
       (b) capability-only note IF a real relationship exists
       on record, with no case study claim at all; or
       (c) walk away and file the scores as do not pursue for
       outreach purposes.
```

## Tree 2: Channel choice

```
START: Match grade is STRONG or PARTIAL and no no-contact flag
applies. Work the routes in order. Do not use more than one
route for the opener.
|
|-- IF a genuine warm introduction path exists (a mutual
|   connection who knows the buyer and the sender, recorded in
|   the inputs, not inferred from a shared connection list)
|   THEN route = WARM INTRO FIRST
|   -> EXIT: Draft the introduction request to the mutual
|      connection, not to the target, per playbook.md: ask in
|      the first two lines, one forwardable paragraph they
|      can paste, an explicit easy out. If they decline or do
|      not reply within a reasonable window set by the human,
|      log it and re-enter this tree at the email branch.
|
|-- IF no warm intro path, AND the buyer's email address is
|   verified from a legitimate source (supplied by the user,
|   published for business contact, or from real prior contact),
|   AND email is not ruled out by channel constraints
|   THEN route = EMAIL
|   -> EXIT: Draft the full email opener per the anatomy.
|      Email is the default and fullest form. Human reviews
|      and sends from their own address.
|
|-- IF no legitimate email route, OR the buyer is publicly
|   active on LinkedIn in a professional context and prior
|   contact happened there, AND LinkedIn is not ruled out
|   THEN route = LINKEDIN DM
|   -> EXIT: Draft the shortened LinkedIn form per playbook.md:
|      under 60 words, no attachments. If no connection exists,
|      draft the connection request note variant instead
|      (under 200 characters, no full pitch, no meeting ask).
|      Manual sending only. No scraping, no automation.
|
|-- IF no warm intro path, no verified email from a legitimate
    source, and no appropriate LinkedIn route
    THEN route = NO LEGITIMATE ROUTE
    -> EXIT: DO NOT BUY OR SCRAPE DATA. Do not guess an email
       pattern, do not use a colleague's account, do not message
       a personal channel. Return the account to research with
       "identify a legitimate contact route" recorded as the
       action and a review date set.
```

## Tree 3: Follow-up cadence and stop rules

```
START: Opener has been approved and sent by the human. Bumps are
drafted as a set of 3. This tree governs each bump and overrides
any default cadence in playbook.md.
|
|-- IF an opt-out, unsubscribe request, or hostile reply has
|   been received at any point, on any channel
|   THEN status = STOP IMMEDIATELY
|   -> EXIT: STOP. No further bumps on any channel. Handle the
|      reply under Tree 4. Log opt-out and do-not-contact where
|      requested. Do not draft a further message to argue or
|      to ask why.
|
|-- IF an out-of-office reply gives a return date, OR a reply
|   or reliable signal says "not now" with a timing cue
|   THEN status = PAUSE AND RESTART ON TRIGGER
|   -> EXIT: PAUSE the sequence. Do not send bumps into an
|      absence. Record the return date or named trigger, set
|      the restart date a few business days after it, log the
|      pause, and restart only with a fresh human review. A
|      "not now" reply is also handled under Tree 4.
|
|-- IF a gatekeeper response is received (an assistant, a team
|   inbox, or a colleague replying on the buyer's behalf)
|   THEN status = ENGAGED, ROUTE VIA GATEKEEPER
|   -> Continue only as the gatekeeper directs: send what they
|      ask for (usually the matched mini-portfolio under Tree 4),
|      to the address or person they name, once. Do not bypass
|      them to the buyer on another channel in the same week.
|      If they decline on the buyer's behalf, treat it as a
|      brush-off under Tree 4 and stop unless they name a
|      future trigger.
|
|-- IF there is engagement short of a reply (for example a
|   forward the user can verify, a profile or asset view the
|   user reports, or a partial reply that asks a question)
|   THEN status = ENGAGED, NO REPLY YET
|   -> Continue the sequence at the planned cadence, but bring
|      the next bump forward only if a dated deadline in the
|      brief justifies it. Answer any direct question by reply
|      draft under Tree 4 first. Do not reference tracking the
|      buyer may not know about or consent to in any draft.
|
|-- IF no engagement at all AND bumps sent < 3
|   THEN status = CONTINUE SEQUENCE
|   -> Send the next bump at its planned spacing (Bump 1 at 4
|      to 5 business days after the opener, Bump 2 at 5 to 7
|      business days after Bump 1, Bump 3 at 7 to 10 business
|      days after Bump 2, adjusted per playbook.md). Each bump
|      must add new value and stand alone. Never send a bump
|      whose only content is a reminder.
|
|-- IF all 3 bumps have been sent with no engagement
    THEN status = SEQUENCE COMPLETE, NO ENGAGEMENT
    -> EXIT: STOP. Log the outcome with the full sequence
       record and the match used. Hand the account to Revive
       and Referral with a future date set by the human. Do
       not draft a Bump 4.
```

## Tree 4: Reply triage

```
START: A reply has been received. The skill drafts the response.
The human reviews and sends every reply. Triage in order: hostile
and opt-out outrank all other categories.
|
|-- IF the reply is hostile, abusive, or a clear opt-out
|   ("remove me", "do not contact again", or equivalent)
|   THEN category = HOSTILE / OPT-OUT
|   -> EXIT: Apologise once, briefly, with no defence and no
|      new pitch. Confirm removal. Log do-not-contact at once.
|      Never argue, never explain the targeting, never send
|      any further message on any channel.
|
|-- IF the reply points to a colleague ("speak to [name]",
|   "this sits with our [role]", or a forwarded introduction)
|   THEN category = REFERRAL
|   -> EXIT: Thank the referrer in a drafted reply within one
|      business day. Ask for an introduction, or for permission
|      to use their name, and do not use their name without it.
|      Treat the new contact as a fresh intake: new sender
|      record, referral recorded as origin, match and channel
|      re-checked under Trees 1 and 2 before any opener.
|
|-- IF the reply is positive (asks for a meeting, expresses
|   interest, asks a substantive question about the matched
|   work or timing)
|   THEN category = POSITIVE
|   -> EXIT: Draft a reply within one business day that answers
|      what was asked, restates the small specific next step
|      (date options for the agreed call length, or the matched
|      material offered), and adds no new claim. On a booked
|      meeting, prep the handoff to the Discovery Call Kit:
|      approved sent outreach, full thread, brief, and match
|      record.
|
|-- IF the reply is a brush-off, identify which kind. Each kind
    has distinct handling. Do not treat them as one category.
    |
    |-- IF "send portfolio", "send some work", or equivalent
    |   THEN handling = MATCHED MINI-PORTFOLIO
    |   -> Send, as a human-approved reply draft, the matched
    |      mini-portfolio only: the matched case study at its
    |      permission level, with its available assets, plus
    |      one question that ties back to the trigger (for
    |      example, whether the timing in the brief is right).
    |      Do not send the whole deck. Log what was sent.
    |
    |-- IF "not now", "bad timing", "next year", or equivalent
    |   with no meeting and no referral
    |   THEN handling = RETURN ON A NAMED TRIGGER
    |   -> Draft a short acceptance. Ask permission to return
    |      on a named trigger (a reset date, a launch, a season,
    |      or a date they name). Log the trigger and date as
    |      agreed. Stop the current sequence. No further bumps.
    |
    |-- IF "we have an agency", "we use an incumbent", or
        equivalent
        THEN handling = INCUMBENT, GRACEFUL EXIT
        -> Draft an acknowledgement with no criticism of the
           incumbent. Ask one question: what would have to
           change for a conversation to be worth having. Then
           exit gracefully whether they answer or not. Log any
           condition they name as a watchlist trigger. Stop
           the current sequence.
```
