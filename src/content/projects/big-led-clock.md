---
title: Big LED Clock & Sports Timer
tagline: A large seven-segment display driven by shift registers, doubling as a count-up match timer.
year: '2022'
status: active
domain: Instrumentation
order: 6
tech: ['7-segment displays', 'Shift registers', 'ESP32', 'NTP']
highlights:
  - Large-format segment display readable across a room
  - Segment mapping and driver wiring worked out per digit before soldering
  - Doubles as a sports timer with explicit minute/second rollover handling
---

A wall clock that is also a match timer. The display is built from large seven-segment digits
driven through shift registers, which keeps the pin count down to something an ESP32 can
handle while still addressing every segment individually.

Most of the design work for this project was segment mapping — working out which driver output
lands on which segment of which digit, which is tedious and completely unforgiving if you get
it wrong after soldering.

The timer logic is deliberately explicit about rollover in both directions: at 60 seconds the
second counter resets and the minute increments, and counting down past zero clamps rather
than wrapping to 59. Writing both cases out by hand first was faster than debugging a display
that briefly shows `-1`.
