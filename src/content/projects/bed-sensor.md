---
title: Bed Occupancy Sensor
tagline: Load cells under the bed legs so the house knows when I actually go to sleep, instead of guessing from a timer.
year: '2023'
status: active
domain: Instrumentation
order: 4
tech: ['Load cells', 'HX711', 'ESP32', 'PIR', 'Home Assistant']
highlights:
  - Occupancy measured by weight rather than motion, so lying still still counts
  - Goodnight fires after 30 minutes in bed, and only once it is past 22:00
  - Goodmorning fires when the bed goes empty after 06:00
  - Under-bed night lights on motion; reading lights behind the headboard
---

Every presence-based automation I had tried failed the same way: a PIR sees you get into bed
and then stops seeing you, so the house decides the room is empty. Weight does not have that
problem. Four load cells, one under each 43 × 43 mm bed leg, give a continuous occupancy
signal that does not care whether you move.

## The rules it drives

- **Goodnight** — triggers after the bed has been occupied for 30 continuous minutes *and*
  the time is past 22:00. The 30-minute delay is what separates going to sleep from sitting
  down to put socks on; the time-of-day guard stops an afternoon nap from shutting the house down.
- **Goodmorning** — triggers when the bed becomes unoccupied after 06:00.
- **Under-bed night lights** — come on for motion, or when the bed becomes unoccupied while
  night mode is active. Getting up at 3am should light the floor, not the room.
- **Reading lights** behind the headboard, on the same controller.

Tracking the nightly weight trend also comes free once the load cells are there, which is a
quieter but more interesting output than the automations.

The interesting part of this project is almost entirely in the trigger conditions rather than
the hardware. Getting a bed sensor to read is easy; getting it to never fire goodnight at the
wrong moment took several rounds of adding guards.
