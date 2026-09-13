---
title: ESP-01 Relay Module
tagline: The smallest useful node — one ESP-01, one relay, one button.
year: '2021'
status: shipped
domain: Home Automation
order: 12
tech: ['ESP-01', 'Relay', 'Momentary button']
highlights:
  - Minimum viable smart switch, small enough to fit inside an existing fitting
  - Local button wired in parallel with network control
---

The baseline node that most of the other home automation projects here grew out of. An ESP-01
is barely a development board — two usable GPIOs and an awkward 3.3 V-only supply — but that
is exactly enough for one relay and one button, and it fits in places a full ESP32 board does
not.

Worth knowing before building one: the ESP-01's two GPIOs are also its boot-mode straps, so
whatever is attached to them must not pull them the wrong way at power-up. That constraint is
what pushed later projects onto the ESP32 and eventually into the
[ESP Connection Board](/projects/esp-connection-board) pin study.
