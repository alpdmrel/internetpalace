---
title: Seaside Outdoor Sensor Module
tagline: A battery-powered outdoor node for soil moisture and climate, built to survive salt air.
year: '2021'
status: shipped
domain: Instrumentation
order: 10
tech: ['ESP32', 'Soil moisture', 'Temperature / humidity', 'Battery', 'Deep sleep']
highlights:
  - Soil moisture plus temperature and humidity on a single battery-backed node
  - Direct VBAT monitoring so the battery state is reported, not assumed
  - Deep sleep between readings — the only way a node like this lasts a season
---

An outdoor sensing node for a seaside garden, which is a harsher environment than it sounds:
constant salt aerosol attacks connectors and exposed copper far faster than an inland
installation.

The electrical design is simple — soil moisture on one ADC channel, temperature and humidity
on a digital sensor, pull-ups on the sensor lines, and a divider bringing VBAT into its own
channel so the module reports its own battery state instead of dying silently.

The engineering effort is in the power budget rather than the circuit. A node like this is
only useful if it runs a whole season on one battery, which means it spends almost all of its
life in deep sleep and wakes only long enough to sample and transmit.
