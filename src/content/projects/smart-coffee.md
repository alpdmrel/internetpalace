---
title: Smart Coffee
tagline: A filter coffee machine rebuilt around an ESP32, with closed-loop brew temperature and voice control.
year: '2023'
status: active
domain: Home Automation
featured: true
order: 1
tech: ['ESP32-WROOM-32', 'K-type thermocouple', 'DS18B20', 'Dosing pump', 'NeoPixel', 'Alexa', 'Home Assistant']
highlights:
  - Brews at a regulated 97.5–98 °C using a K-type thermocouple polled every 200 ms
  - Keep-warm holds 65–67 °C so the pot never turns bitter, then idles out after 90 minutes
  - Detects the filter basket magnetically and starts brewing on its own
  - Voice or web UI front end — the machine asks how many cups before it grinds
---

I wanted coffee to be waiting for me rather than something I had to go and start. So the
machine got opened up and rebuilt: every component that used to be behind a button is now
behind an ESP32, and the original front panel became a capacitive input surface.

## How a brew runs

The user picks a drink through Alexa or the web UI, and the system asks the questions it
actually needs — filter or espresso, how many cups, whether there are guests. From there it
runs unattended:

1. The grinder's grind-size and dose knobs are driven to the settings for that drink, and grinding starts.
2. In parallel, a dosing pump meters the matching volume of water into the machine's reservoir.
3. When both finish, the user is notified by voice and mobile push.
4. The only manual step left: drop a filter and the grounds into the basket. Sliding the basket back in is detected by a magnetic field sensor, which switches the machine into **Brewing**.
5. Brewing is held between 97.5 and 98 °C. A non-contact water sensor watches the tank; when it runs dry, brewing stops and the machine moves to **Keep Warm** at 65–67 °C.
6. After an hour and a half it drops to **Idle**, either on that timer or by holding the program button.

## Telling the machine what it's doing

The original power button was rewired as an RGB status light, so the machine's state is
readable from across the room:

| Indication | Meaning |
| --- | --- |
| Pulsing red and orange | Brewing |
| Solid white | Coffee ready, keeping warm |
| Pulsing blue at startup | Water tank is empty |
| Off | No power, or idle |

Overheating triggers a shutdown plus a push notification, and deliberately requires a manual
inspection and a three-second program-button hold before it will reset — I did not want a
thermal fault to be something the machine could quietly clear by itself.

An **Auto** light distinguishes the two operating modes. In auto, the tank and basket
interlocks cannot be overridden. Manual mode disables both, which is strictly for bench
testing.

## Build notes

One ESP32 drives two relays, the filter-coffee water pump, the grinder, two Dallas temperature
probes, an ultrasonic level sensor and two LED strips — plus a dog feeder that got adopted into
the same controller because it was already in the right cupboard. Signal inputs run through
BC547 transistors, and every subsystem terminates in a keyed 6-pin connector so the machine can
still be taken apart.

The six capacitive pads were calibrated by hand — each one has a different untouched baseline
(0 to 630 counts) and a different pressed threshold, so the firmware stores per-pad values
rather than one global trigger point.
