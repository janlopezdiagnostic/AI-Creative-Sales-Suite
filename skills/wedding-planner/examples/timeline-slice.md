# Example: timeline slice + a flagged conflict

## Input (from intake)

- Ceremony 4:00pm, garden venue; reception same venue from 5:00pm
- Bride + 5 bridesmaids, hair and makeup, 2 artists (1 hair, 1 makeup), starting 10:00am at a hotel 25 min away
- Couple wants: first look at the venue, family photos after the ceremony, sunset portraits
- Sunset on the date: 7:42pm
- Caterer doors / guest arrival: 5:00pm; plated dinner; DJ booked for the reception

## Output - conflict flagged first

**Conflict:** the intake lists 2 artists, one on makeup and one on hair. Makeup is the bottleneck: 6 people x ~50 min = 5 hours, so a 10:00am start finishes makeup at ~3:00pm, after the 2:30pm departure needed to make a 3:10pm first look (25 min drive + 50% padding). Zero slack, and the first look dies. Fixes, pick one: (a) start at 8:30am, (b) add a third artist, (c) drop the venue first look and do it at the hotel. Recommend (a) if the party will tolerate the early start, (b) if not.

## Output - master timeline (slice, assuming fix (a): 8:30am start, same 2 artists)

- 8:30am - Hair & makeup begins (hotel), bride scheduled second-to-last, never last
- 1:30pm - Makeup done (8:30 + 5h); hair finished inside the same window
- 1:45pm - Touch-ups and dressing done; 45-min buffer held for overruns
- 2:30pm - Depart hotel (25 min drive + 50% padding = 40 min block)
- 3:10pm - Arrive venue; first look in the garden
- 3:40pm - Wedding party photos; couple rests, room check
- 4:00pm - Ceremony
- 4:30pm - Family photos, oldest relatives first and released to the reception
- 5:00pm - Guests seated for reception (caterer had the room from 3:30pm for their 90-min load-in; room ready 4:30pm)
- 7:30-7:50pm - Sunset portraits (sunset 7:42pm), couple steps out between courses

## Output - rain pivot (garden ceremony)

If rain is called by 12:00pm: ceremony moves to the reception room, caterer flips it during family photos (adds 20 min, pushing reception seating to 5:20pm), first look moves to the covered porch at 3:10pm, sunset portraits become porch portraits at the same time.

## Output - vendor brief (photographer, slice)

"First look 3:10pm in the garden, party photos 3:40-4:00, family groups 4:30-5:00 in this order: [list], grandparents released first. Sunset window is protected: 7:30-7:50pm, couple will step out during the DJ's long set."
