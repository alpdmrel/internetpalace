---
title: Blackout Announcement System
tagline: PoE-backed emergency announcements and lighting that survive the outage they exist to announce.
year: '2021'
status: on-hold
domain: Power
order: 21
tech: ['PoE', 'Battery backup', 'TTS', 'Emergency lighting']
highlights:
  - Text-to-speech announcement over the house audio when mains drops
  - Battery backup fed through PoE so the node stays up with the network
  - Audio path switches to a battery-powered speaker on loss of mains
  - Emergency lighting on the same backup domain
---

A system whose entire job happens during a power cut has an obvious bootstrapping problem: it
has to outlive the event it is reporting. The approach here is to hang everything off the PoE
domain, which is already battery-backed for the network, rather than building a separate UPS.

On loss of mains the node announces the outage by text-to-speech, switches the audio path from
the normal house speakers to a battery-powered one, and brings up emergency lighting.

## Why it is on hold

The design is sound but the power budget was never properly measured. "Battery backup" is only
meaningful with a number attached — how long, driving what load — and until the announcement
speaker and lighting are characterised under real discharge, the runtime claim is a guess.
Parked until that measurement is done.
