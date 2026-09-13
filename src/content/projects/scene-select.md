---
title: Scene Select
tagline: One controller, five lighting modes — the layer that made every other light in the flat worth automating.
year: '2021'
status: shipped
domain: Home Automation
order: 8
tech: ['ESP8266', 'Home Assistant', 'Scene control']
highlights:
  - Five modes — movie, ambient, daytime, night light and work
  - Each mode sets several fixtures at once rather than toggling one
---

Individually controllable lights are only useful once something coordinates them. Scene Select
is that layer: five modes, each setting a group of fixtures to a defined state.

| Mode | What it sets |
| --- | --- |
| Movie | Everything dimmed down |
| Ambient | Indirect lighting plus the TV backlight |
| Daytime | Desk beam light to 100% |
| Night light | Beam light at low level, bed lamp on |
| Work | Desk lamp and desk beam light both at 100% |

The list looks trivial written out, which is the point — the value is that "movie" is one
action instead of five, and the definition of what movie means lives in one place that can be
changed later.
