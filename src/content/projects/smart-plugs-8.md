---
title: 8-Way Smart Plug Bank
tagline: Eight individually switched and metered outlets in one 150 × 138 × 56 mm enclosure.
year: '2021'
status: shipped
domain: Power
order: 11
tech: ['ESP32', 'Relay bank', 'Energy metering', '3D printed enclosure']
highlights:
  - Eight independently switched outlets from one controller and one mains feed
  - Custom enclosure designed around the relay bank and creepage clearances
  - Physical button retained alongside network control
---

Commercial smart plugs are one relay and one ESP each, in a housing far larger than the
electronics need, and eight of them means eight things to provision. This is one controller,
one mains feed and one enclosure driving eight independently switched outlets.

The enclosure is the hard part rather than the firmware. At 150 × 138 × 56 mm it has to fit
eight relays, the switched and neutral busbars, the controller and the low-voltage supply,
while keeping mains creepage and clearance distances intact between channels and away from
anything a person can touch. Most of the design time went into that packing problem rather than
the electronics.

As with every mains project here, the physical button stays in the circuit — network control
is an addition to the switch, never a replacement for it.
