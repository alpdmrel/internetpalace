---
title: Clock Shelf
tagline: A shelf that is also the enclosure for the clock — structure and housing as one part.
year: '2021'
status: on-hold
domain: Mechanical
order: 24
tech: ['CAD', 'Woodwork', 'ESP32']
highlights:
  - Controller and wiring concealed inside the shelf structure itself
  - Segment and module spacing laid out arithmetically before cutting
---

The companion piece to the [LED clock](/projects/big-led-clock): rather than mounting a
display box onto a shelf, the shelf *is* the enclosure. The ESP32 and wiring live inside the
structure, so nothing is visible except the digits.

Most of the work is layout arithmetic — dividing the available span into equal modules and
checking the totals before anything gets cut, since the spacing has to come out even across the
full width or the display looks wrong.

## Why it is on hold

It is blocked on the clock itself. Building the enclosure before the display's final dimensions
are fixed means building it twice, so this waits for the clock to be finished.
