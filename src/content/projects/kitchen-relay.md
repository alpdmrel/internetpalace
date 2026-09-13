---
title: Kitchen Relay & Sensor Node
tagline: Mains switching plus climate sensing on one small board behind the kitchen wall plate.
year: '2021'
status: shipped
domain: Power
order: 9
tech: ['ESP8266', 'BMP280', 'Relay', 'Status LED']
highlights:
  - Relay switching with the existing wall button still wired through
  - BMP280 for temperature and pressure in the same enclosure
  - Status LED on the faceplate
---

A retrofit node that fits behind an existing kitchen wall plate. The relay does the switching,
and the original physical button stays wired as an input — so the light works normally if the
network is down, which is non-negotiable for anything mains-connected in a room you use daily.

A BMP280 rides along on the same board for temperature and pressure, on the reasoning that if
a board is already going into the wall with power available, it may as well report something.
The one compromise is that a sensor sharing an enclosure with a switching relay reads a little
warm — it is fine for trend data, less so for absolute accuracy.
