---
title: ESP Connection Board
tagline: A breakout board, and the GPIO survey behind it — which ESP32 pins are actually safe to use.
year: '2023'
status: archived
domain: Instrumentation
order: 14
tech: ['ESP32-WROOM-32', 'Breakout PCB', 'GPIO mapping']
highlights:
  - Full audit of the ESP32's 38 pins down to the 21 that are genuinely free
  - Documents input-only pins, boot-strapping pins and pins that glitch at reset
  - Superseded by per-project boards, but the pin map still gets used
---

Every ESP32 project starts with the same hour of work: figuring out which pins you are allowed
to use. The datasheet lists 38, but a large fraction are spoken for, and the failure modes are
subtle — a board that works on the bench and then refuses to boot once a sensor is plugged in.

The notes for this project are that audit written out once, properly:

- **Input only** — GPIO 34, 35, 36 and 39 have no output driver and no internal pull-ups, so anything on them needs external resistors.
- **Boot straps** — GPIO 12 fails to boot if pulled high; others must be left alone at reset.
- **PWM at boot** — several pins output a pulse during startup, which means anything that must not twitch at power-up cannot live there.
- **Prefer not to use** — the flash interface pins, which are not free at all.

That leaves **21 genuinely usable I/O**, and any button or switch needs its own pull-up.

The board itself has been **superseded** by task-specific boards for each project, so it is
archived rather than active. The pin map, though, is still the first thing I open when starting
anything on an ESP32 — which is a reasonable outcome for a board that did not survive.
