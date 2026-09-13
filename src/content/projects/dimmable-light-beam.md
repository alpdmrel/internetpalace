---
title: Dimmable Light Beam
tagline: A PWM-dimmed LED beam on a custom PCB, switched by motion — the first board of mine that went straight from sketch to etch.
year: '2022'
status: shipped
domain: Power
featured: true
order: 7
tech: ['TIP122 Darlington', 'PWM', 'Custom PCB', 'PIR', 'ESP8266']
highlights:
  - Single TIP122 NPN Darlington handling the LED current, gated by PWM
  - Purpose-made PCB replacing the breadboard prototype
  - Motion-triggered, with the brightness level set by scene rather than fixed
---

The smallest project on this site and the one I still use most. A 12 V LED beam, dimmed by
PWM through a TIP122 NPN Darlington, on a board made specifically for it rather than the
usual perfboard.

A Darlington is not the efficient choice here — the two junction drops cost more headroom than
a MOSFET would — but it is forgiving of the gate drive and it was in the parts drawer. For a
fixture that draws what this one does, the simplicity won.

The version in daily use is motion-triggered, with the brightness set by whichever scene is
active rather than being a fixed level, so the same fixture works as a night light and as a
task light. It is also the light driven at 100% by the [Scene Select](/projects/scene-select)
controller's work and daytime modes.
