"""Pull the figures out of the hydroponic thesis and caption them in English.

The thesis itself is a 62-page Turkish document and is not published on the
site — only its figures are, each with an English caption written here. Images
are addressed by PDF xref so that the mapping stays stable and nothing depends
on page-scrape ordering.

The source PDF is encrypted with an empty owner password, hence the
authenticate("") call.

Outputs:
  public/figures/<slug>/NN.webp        full-size
  public/figures/<slug>/NN.thumb.webp  gallery thumbnail
  src/data/figures.json                manifest consumed by the Astro pages

Run with:  npm run figures
"""

import io
import json
import os
import shutil
import sys

import pymupdf
from PIL import Image

SLUG = "hydroponic-automation"
SRC = r"H:\My Drive\Alp\School\Tasarim Projesi 1\AlpDEMİREL_HidroponikSistemOtomasyonu.pdf"

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "public", "figures", SLUG)
MANIFEST = os.path.join(REPO, "src", "data", "figures.json")

FULL_WIDTH = 1500
THUMB_WIDTH = 520

# xref -> (figure number, English title, English explanation)
#
# Titles are translations of the thesis captions; the explanations are written
# for a reader who has not read the thesis. Cover logos, 2x2 spacer pixels and
# the low-resolution simulation-parameters screenshot are deliberately omitted.
#
# Figures 1, 3, 6, 7 and 8 are NOT listed here. Those are the Turkish block
# diagrams, and they are redrawn in English as SVG by build_diagrams.py — see
# src/components/SystemDiagrams.astro. Only photographs, screenshots and
# already-English figures are rasterised from the PDF.
FIGURES = [
    (76, 2, "Types of hydroponic system",
     "The six growing methods surveyed before choosing one — nutrient film, deep "
     "water culture, ebb and flow, drip, aeroponics and the conventional variant. "
     "Each places different demands on the controller."),
    (98, 4, "Dallas temperature sensor",
     "The waterproof 1-Wire probe used for water temperature. 1-Wire lets several "
     "probes share a single data line, which matters when sensors are spread across "
     "a tank, a feed line and the air above the crop."),
    (103, 5, "Turbidity sensor — voltage against cloudiness",
     "The sensor's transfer curve. Turbidity indicates algae growth or particulate "
     "contamination in the nutrient solution, both of which foul the pumps."),
    (145, 9, "Hydroponic growing pipe",
     "The growing channel itself, with the net-pot spacing that sets how many "
     "plants a run supports and how much root mass the flow has to feed."),
    (148, 10, "pH solutions, A&B nutrient and dosing pumps",
     "The correction chemistry: pH-up and pH-down solutions plus the two-part A&B "
     "nutrient concentrate, each on its own dosing pump. A and B must be dosed "
     "separately — mixed at concentration they precipitate out of solution."),
    (153, 11, "pH regulation algorithm",
     "The control loop for pH, implemented as a state machine. If the reading sits "
     "outside the configured window the matching pump runs for five seconds, then the "
     "loop waits thirty before reading again. That settle time is the whole design: "
     "dosing faster than the tank mixes is exactly how a pH controller ends up "
     "oscillating between over-corrections."),
    (157, 12, "A&B nutrient regulation algorithm",
     "Nutrient strength is controlled against electrical conductivity: EC rises as "
     "dissolved salts increase, so it stands in for concentration. A and B are dosed "
     "in a fixed ratio and the loop waits for the reading to settle."),
    (161, 13, "Tank water level regulation algorithm",
     "Level control, and the reason nutrient dosing is sequenced after it: topping up "
     "with plain water dilutes the solution, so EC has to be corrected after the "
     "level is right, never before."),
    (170, 15, "Simulation — view 1",
     "The system modelled before hardware was committed, to check that the control "
     "loops behave at realistic tank volumes and dosing rates."),
    (173, 16, "Simulation — view 2",
     "A second simulation view covering the interaction between level, EC and pH "
     "regulation running together."),
    (184, 17, "pH sensor calibration",
     "Calibration against buffer solutions. A pH probe drifts as its glass membrane "
     "ages, so periodic recalibration is a maintenance requirement, not a one-off "
     "setup step."),
    (189, 18, "Control panel — interior",
     "The assembled controller: supplies, relays and terminal blocks, with low-voltage "
     "signal wiring kept away from the switched mains side."),
    (192, 19, "Control panel — inner cover",
     "The inner cover, which keeps the mains section out of reach while the "
     "low-voltage side is being worked on."),
    (193, 20, "Control panel — exterior",
     "The finished enclosure as installed."),
    (196, 21, "Light measurement hardware",
     "The light sensing head as built, positioned at canopy height where the "
     "measurement is actually meaningful."),
    (199, 22, "Water tank and measurement instruments",
     "The tank with the pH, EC and level instrumentation installed in the "
     "circulation path."),
]


def save(img: Image.Image, path: str, width: int) -> tuple[int, int]:
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    if img.width > width:
        height = round(img.height * width / img.width)
        img = img.resize((width, height), Image.LANCZOS)
    img.save(path, format="WEBP", quality=84, method=5)
    return img.width, img.height


def main() -> int:
    if not os.path.exists(SRC):
        print(f"missing source: {SRC}")
        return 1

    doc = pymupdf.open(SRC)
    if doc.is_encrypted:
        doc.authenticate("")

    if os.path.isdir(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    os.makedirs(OUT_DIR, exist_ok=True)

    entries = []
    for xref, number, title, explanation in FIGURES:
        try:
            raw = doc.extract_image(xref)
        except Exception as exc:
            print(f"  !! xref {xref} ({title}): {exc}")
            continue

        img = Image.open(io.BytesIO(raw["image"]))
        name = f"{number:02d}.webp"
        thumb = f"{number:02d}.thumb.webp"
        w, h = save(img, os.path.join(OUT_DIR, name), FULL_WIDTH)
        save(img, os.path.join(OUT_DIR, thumb), THUMB_WIDTH)

        entries.append(
            {
                "number": number,
                "title": title,
                "explanation": explanation,
                "src": f"/figures/{SLUG}/{name}",
                "thumb": f"/figures/{SLUG}/{thumb}",
                "width": w,
                "height": h,
            }
        )
        print(f"  Fig {number:>2}  {title}")

    doc.close()

    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump({SLUG: entries}, f, indent=2, ensure_ascii=False)

    print(f"\n{len(entries)} figure(s) -> {MANIFEST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
