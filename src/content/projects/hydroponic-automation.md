---
title: Hydroponic System Automation
tagline: Senior design thesis — a controller that holds a soil-free growing medium at the right pH, nutrient strength and water level without daily supervision.
year: '2022'
status: research
domain: Academic
featured: true
order: 3
figures: hydroponic-automation
tech: ['ESP32', 'ESP8266', 'Raspberry Pi 4', 'pH probe', 'EC / TDS', 'SHT20', 'Dosing pumps', 'PWM']
highlights:
  - B.Sc. design project at Manisa Celal Bayar University, supervised by Doç. Dr. Yücel Koçyiğit
  - Four field nodes reporting to a Raspberry Pi that holds the database and the control logic
  - Closed-loop pH, nutrient and water-level regulation, sequenced so they do not fight each other
  - Simulated before build, then calibrated and installed as a working panel
---

Hydroponics removes most of the hard parts of growing — it is a closed loop, so water loss is
near zero, and being isolated from the outside means no pesticide. What it does not remove is
effort. The growing medium has to be held at the right pH, nutrient concentration, temperature
and water level, and left alone that is a daily manual chore.

That is a control problem, not an agricultural one. The thesis builds a controller that
regulates the medium automatically after installation.

## Architecture

Measurement stays at the edge and control lives centrally. Four field nodes — two ESP32s for
sensing and actuation, an ESP8266 for lighting, and a fourth for light measurement — report
over the LAN to a Raspberry Pi 4 holding the database, the automations and the interface.

The split matters for reliability: a single node dropping off takes out one measurement rather
than the whole loop, and the control logic can be changed without reflashing anything in the
grow room.

- **Unit 1 — sensing.** pH, EC/TDS, air and water temperature and humidity (SHT20 and AM2315 over I²C, waterproof Dallas probes over 1-Wire), ultrasonic and analogue level, flow, leak, turbidity, and an INA226 power meter.
- **Unit 2 — actuation.** Relays, dosing pumps for nutrient and pH correction, the main circulation pump, air pump and ventilation fans.
- **Unit 3 — lighting.** PWM brightness control through a TIP122 Darlington.
- **Light measurement.** VEML6070 for UV, TCS34725 for colour, TSL2561 for illuminance — closing the loop on the light actually delivered rather than the light nominally switched on.

## The three control loops

The interesting part of the project is that the three regulation loops interact, and the order
they run in is what makes the system stable.

**pH** is corrected by dosing acid or base, then waiting. Each correction runs the pump for
five seconds and then holds for thirty before reading again. Without that settle time the
controller reads a tank that has not finished mixing, over-corrects, and oscillates.

**Nutrient strength** is controlled against electrical conductivity, which rises with dissolved
salt content and therefore stands in for concentration. The A and B concentrates are dosed in a
fixed ratio and separately — mixed at full strength they precipitate out of solution.

**Water level** has to be corrected *before* nutrient strength, never after. Topping the tank
up with plain water dilutes everything in it, so a level correction invalidates the EC reading
that preceded it. Sequencing these the wrong way round produces a system that chases its own
tail.

## Cost as a design constraint

The project was explicitly cost-driven, since the target user was a small grower rather than a
commercial greenhouse. Plastic parts for the pumps and fittings were modelled and 3D printed
rather than bought, and a broad supplier list was built for every sensor and microcontroller so
the bill of materials could be re-sourced to whatever was cheapest at production time.

The system was simulated before any hardware was committed, then calibrated against buffer
solutions and built into a control panel with the mains and low-voltage sections separated.
