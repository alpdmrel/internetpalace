---
title: Raspberry Pi Rack
tagline: A 3D printed stacking rack sized around airflow and cable clearance rather than board outlines.
year: '2022'
status: shipped
domain: Mechanical
order: 13
tech: ['FDM printing', 'CAD', 'Thermal design']
highlights:
  - Module pitch set by cable bend radius, not by board thickness
  - 60 mm cable clearance channel down one side
  - Ventilation gaps between layers for passive convection
---

A stacking rack for the Raspberry Pis running the house. The dimensions are the whole design:
the spacing between layers is not set by how thick a Pi is, but by how much room an HDMI and an
Ethernet cable need to leave the board without being bent past their radius.

The other driver is thermal. A stack of boards in still air is a chimney with no draught, so
each layer is open at front and back to let convection actually move through rather than
trapping warm air between boards. Passive cooling only works if the geometry allows it — a
tighter, better-looking stack would have needed fans.
