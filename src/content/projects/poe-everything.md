---
title: PoE for Everything
tagline: Splitter boxes and 3D printed housings to bring Power-over-Ethernet to devices that were never designed for it.
year: '2021'
status: on-hold
domain: Power
order: 22
tech: ['PoE splitters', '802.3af', '3D printed enclosures', 'Structured cabling']
highlights:
  - One cable per device — data and power together, no local wall wart
  - Receptacle boxes converting PoE to the barrel jack a device expects
  - Printed housings and hand-terminated panel cabling
---

The motivating observation: almost every node in the house needs both a network connection and
power, and running two cables to each one is twice the work and twice the mess. PoE solves it
in principle, but almost nothing consumer-grade accepts it directly.

So the project is a set of receptacle boxes — a PoE splitter in a printed housing that
presents whatever the device actually wants, usually a barrel jack — plus the panel cabling to
terminate them tidily.

The side benefit is the one that matters for
[blackout announcement](/projects/blackout-announcement): PoE devices inherit the network
switch's UPS, so anything on PoE is battery-backed without a battery of its own.

## Why it is on hold

This is infrastructure rather than a device, and it only pays off if it is done everywhere at
once. It is parked until a cabling pass through the whole flat is worth doing in one go.
