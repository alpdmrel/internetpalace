---
title: Keypad Door Lock
tagline: A 4×4 keypad entry system with armed/granted/denied states signalled by light and buzzer.
year: '2021'
status: on-hold
domain: Home Automation
order: 20
tech: ['4×4 matrix keypad', 'ESP32', 'Buzzer', 'RGB indicator', 'Home Assistant']
highlights:
  - Four distinct feedback states — granted, denied, armed, locked
  - Code entry evaluated in Home Assistant, with the lamp driven by template
  - Sloped keypad housing designed for the entry wall
---

A keypad entry system for the front door. The keypad is a standard 4×4 matrix (`123A / 456B /
789C / *0#D`) in a sloped housing so the keys face the person standing at the door rather than
the ceiling.

The design effort went into feedback. A lock that gives no indication is unusable in the dark
and ambiguous in the light, so each state gets its own combination of indicator colour and
buzzer tone: **granted**, **denied**, **armed** and **locked — please activate**.

Code evaluation is handled in Home Assistant, with the keypad publishing its payload as a
sensor and an automation matching it against accepted codes before driving the indicator
brightness and colour.

## Why it is on hold

It works on the bench, but a door lock is the one automation where a failure locks you out of
your own home, and I was not satisfied with the offline behaviour — evaluating codes on the
server means a network outage becomes a lockout. Finishing it properly means moving code
validation onto the device itself, with the server only as a secondary path. That rewrite has
not happened yet, so it stays parked rather than installed.
