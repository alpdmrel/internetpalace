export const site = {
  name: 'Şekip Alp Demirel',
  shortName: 'Alp Demirel',
  role: 'Hardware & Manufacturing Engineer',
  location: 'Tampere, Finland',
  email: 'alpdemirel@protonmail.com',
  phone: '+358 40 444 9408',
  github: 'https://github.com/alpdmrel',
  url: 'https://alpdemirel.tech',
  tagline:
    'I design the boards, the enclosures and the production line that makes them.',
  intro: [
    `Electrical and electronics engineer working on motor control, low-power sensing and the
     manufacturing processes that turn a prototype into a product. Day to day that means
     schematic capture and controlled-impedance layout in Altium, then the mechanical design,
     jigs and work instructions that let someone else build it a hundred times a month.`,
    `Most of what is on this site started as a problem in my own apartment — a coffee machine
     that should have started itself, curtains that should have known the window was open. The
     projects below are written up for the decisions rather than the parts list: what the
     constraint was, what I chose, and where I got it wrong first.`,
  ],
} as const;

export const experience = [
  {
    role: 'Lead Hardware & Mechanical Engineer',
    company: 'AQL Robotics',
    location: 'Tampere, Finland',
    period: '10/2024 — Present',
    points: [
      'Designed and qualified a closed-loop BLDC motor-controller board (CAN-FD, 40 A continuous) with Kelvin-sense shunts, low-noise gate drivers and thermal-via arrays; owned schematic and controlled-impedance layout in Altium, validated with Keysight power analysis.',
      'Produced the full electrical documentation set — schematics, BoM, stack-up, assembly drawings, DFM/DFT checklists — bringing PCBA rework below two percent at launch.',
      'Re-architected the robotic arm around in-house gear reducers, improving modularity and readiness for mass production.',
      'Built lightweight motor modules using SLS housings and metal gearboxes, cutting backlash while increasing rigidity.',
      'Launched in-house BLDC motor manufacturing, from supplier sourcing to first assembly runs.',
      'Completed 3 in-house pilot systems now approved to scale to 100 units per month.',
      'Recruited and led engineers, ran design reviews, and directed compliance research toward CE certification.',
    ],
  },
  {
    role: 'Lead Hardware Engineer & Head of Manufacturing',
    company: 'Taika Tech',
    location: 'Espoo, Finland',
    period: '10/2023 — 09/2024',
    points: [
      'Reduced PCB footprint 30% and added flexibility by migrating from rigid-flex to full-flex in Altium.',
      'Increased touchpad active area 80% and accuracy 90% through a new sensor layout and IC placement.',
      'Doubled wireless range and eliminated EMI after a PSpice-guided antenna redesign.',
      'Cut enclosure volume 40% and achieved waterproofing with epoxy-fill overmolding.',
      'Lowered surface roughness from 16 µm to 0.4 µm with a custom sanding–polishing process.',
      'Raised housing strength ten-fold by integrating a DMLS-printed metal inner ring.',
      'Halved assembly cycle time and boosted throughput 30% with purpose-built jigs and machines.',
    ],
  },
] as const;

export const education = [
  {
    degree: "B.Sc. Electrical and Electronics Engineering",
    school: 'Celal Bayar University',
    location: 'Manisa / İzmir, Turkey',
    period: 'Graduated 12/2023',
  },
] as const;

export const skills = [
  {
    group: 'Hardware',
    items: [
      'PCB Design',
      'Altium Designer',
      'Analog Circuit Design',
      'Low Power Systems',
      'Radio Frequency',
      'Internet of Things',
      'PSpice',
      'Test Automation',
      'Debugging',
    ],
  },
  {
    group: 'Manufacturing',
    items: [
      'SOLIDWORKS',
      'CAD',
      'DFM',
      'DFA',
      'Materials Science',
      'Product Design',
      'Mechanical Assembly',
    ],
  },
  { group: 'Software', items: ['C++', 'JavaScript', 'SCADA', 'ESPHome', 'Home Assistant'] },
  { group: 'Languages', items: ['Turkish — native', 'English — C1'] },
] as const;
