---
title: Macro Keypad
tagline: A desk keypad with tap, hold and sticky layers — one physical key doing three jobs without ambiguity.
year: '2023'
status: active
domain: Home Automation
order: 5
tech: ['Matrix keypad', 'ESP32', 'Home Assistant']
highlights:
  - Three input gestures — tap, hold (≥200 ms) and sticky — layered on the same keys
  - Sticky keys latch like a flip-flop, so a layer stays selected without being held
  - Drives desk, monitor, task lamp and ambient lighting scenes
---

A wall switch has one action per key, which means a desk with six controllable things needs
six switches. Adding layers fixes that, but only if the gestures are unambiguous enough that
you never have to think about them.

## Gesture model

- **Tap** — press and release quickly. The default action.
- **Hold** — 200 ms or longer. Selects a layer while held.
- **Sticky** — latches on like a flip-flop, so a layer can be selected and left selected
  rather than held down with a spare finger.

The 200 ms threshold is the whole design. Shorter and normal taps start registering as holds;
longer and the keypad feels laggy because you are waiting on it to make up its mind.

Sticky mode is what makes the layout usable one-handed — it is the difference between a chord
and a mode. Layers cover the desk light, the monitor backlight, a task lamp and the ambient
scene, each of which is a tap away once the layer is latched.
