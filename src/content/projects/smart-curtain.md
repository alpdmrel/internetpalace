---
title: Smart Curtain
tagline: Three motorised curtain rails on one ESP32, with limit switches, window sensors and a manual override that always wins.
year: '2021'
status: shipped
domain: Home Automation
featured: true
order: 2
tech: ['ESP32', 'Stepper drivers', 'Reed switches', '3D printed brackets', 'Home Assistant']
highlights:
  - Three independent rails — bedroom and two library windows — from a single controller
  - Open and close limit switches per rail, so the firmware never has to trust step counts
  - Reed switch on each window disables motion while the window is open
  - Colour-coded 10-conductor harness, documented pin by pin
---

Curtains are the one piece of home automation everyone actually notices, and the commercial
motors were both expensive and single-rail. This drives three of them from one board.

## Channel layout

Each rail gets the same six signals — `STEP`, `DIR`, `SLEEP`, an open limit switch, a close
limit switch and a manual control input — plus a window sensor. All three channels are mapped
onto one ESP32:

| Rail | STEP | DIR | SLEEP | Open SW | Close SW | Manual | Window |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bedroom | 22 | 21 | 23 | 19 | 18 | 36 | 26 |
| Library 1 | 33 | 32 | 25 | 35 | 34 | 39 | 27 |
| Library 2 | 16 | 4 | 17 | 15 | 14 | 12 | 13 |

The `SLEEP` line matters more than it looks: stepper drivers idle hot and noisy, and a curtain
spends essentially all day parked. Dropping the driver into sleep between moves keeps the
rails silent and cool.

## Why limit switches

Position could have been tracked in software by counting steps, but a curtain is a friction
system — fabric binds, a missed step accumulates, and after a week the rail drives itself into
the end stop. Physical open and close switches make the end positions self-correcting: every
full travel re-zeros the axis, so drift can never build up.

The window reed switch is an interlock rather than an automation input. If the window is open,
the curtain does not move — this avoids the failure mode where a curtain closes onto an open
sash and stalls the motor.

## Harness

Each rail terminates in a 10-way connector with a fixed colour code (1/2 for coil A, 3/4 for
coil B, then open, close, manual, ground, window, and a spare), with the cable mesh bonded to
ground. Writing the colour map down in the notebook before crimping is the only reason the
third rail took twenty minutes instead of an afternoon.
