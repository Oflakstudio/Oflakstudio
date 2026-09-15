#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manish Kumar — one-page CV (dark theme, lime accents).
Rebuilds the ReportLab generator to match the existing Manish-Kumar-CV.pdf and
applies the 2026-08 updates: 16+ brands, 13 industries, two new projects in
Selected Work, enriched Suprams line, broadened profile. Nothing invented —
content drawn from resumeData.ts + the Suprams case-study board.
"""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---- fonts ---------------------------------------------------------------
FONTS = {
    "Sans":       "/usr/lib/python3/dist-packages/mkdocs/themes/readthedocs/fonts/Lato-Regular.ttf",
    "Sans-Bold":  "/usr/lib/python3/dist-packages/mkdocs/themes/readthedocs/fonts/Lato-Bold.ttf",
    "Sans-Light": "/usr/lib/ruby/3.0.0/rdoc/generator/template/darkfish/fonts/Lato-Light.ttf",
    "Sans-It":    "/usr/lib/python3/dist-packages/mkdocs/themes/readthedocs/fonts/Lato-Italic.ttf",
    "Mono":       "/usr/lib/ruby/3.0.0/rdoc/generator/template/darkfish/fonts/SourceCodePro-Regular.ttf",
    "Mono-Bold":  "/usr/lib/ruby/3.0.0/rdoc/generator/template/darkfish/fonts/SourceCodePro-Bold.ttf",
}
for name, path in FONTS.items():
    pdfmetrics.registerFont(TTFont(name, path))

# ---- palette -------------------------------------------------------------
BG      = HexColor("#02050B")
SURFACE = HexColor("#080D19")
LIME    = HexColor("#CFF07C")
WHITE   = HexColor("#FFFFFF")
BODY    = HexColor("#C7CDD6")
GREY    = HexColor("#7E8794")
RULE    = HexColor("#20242E")

PAGE_W, PAGE_H = A4
M = 44.0
CW = PAGE_W - 2 * M

c = canvas.Canvas(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Manish-Kumar-CV.pdf"), pagesize=A4)
c.setTitle("Manish Kumar — Graphic & Visual Communication Designer — CV")
c.setAuthor("Manish Kumar")
c.setSubject("Curriculum Vitae")
c.setCreator("Crea Graphix")

def T(y):  # top-origin helper
    return PAGE_H - y

def width_of(s, font, size, cs=0.0):
    w = pdfmetrics.stringWidth(s, font, size)
    if cs and len(s) > 1: w += cs * (len(s) - 1)
    return w

def text(x, y, s, font="Sans", size=10, color=BODY, cs=0.0, align="l"):
    c.setFillColor(color)
    if align == "r":   x -= width_of(s, font, size, cs)
    elif align == "c": x -= width_of(s, font, size, cs) / 2.0
    to = c.beginText(x, T(y))
    to.setFont(font, size)
    to.setFillColor(color)
    to.setCharSpace(cs)
    to.textOut(s)
    c.drawText(to)

def rule(x1, y, x2, color=RULE, w=0.8):
    c.setStrokeColor(color); c.setLineWidth(w)
    c.line(x1, T(y), x2, T(y))

def sq(x, y, s=4.2, color=LIME):
    c.setFillColor(color); c.rect(x, T(y) - s + 1, s, s, stroke=0, fill=1)

def heading(x, y, label, right=None):
    """lime square + mono uppercase lime label, optional thin rule to `right`."""
    sq(x, y)
    text(x + 9, y, label, font="Mono-Bold", size=7.6, color=LIME, cs=1.6)
    if right:
        lw = width_of(label, "Mono-Bold", 7.6, 1.6)
        rule(x + 9 + lw + 10, y - 2.2, right, color=RULE, w=0.7)

# ============================ background =================================
c.setFillColor(BG); c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
# faint grid texture
c.setStrokeColor(HexColor("#0B111C")); c.setLineWidth(0.4)
step = 26
x = 0
while x <= PAGE_W:
    c.line(x, 0, x, PAGE_H); x += step
y = 0
while y <= PAGE_H:
    c.line(0, y, PAGE_W, y); y += step

# ============================ header =====================================
text(M, 72, "CREATIVITY.  SIMPLIFIED.", font="Mono-Bold", size=8.2, color=LIME, cs=2.2)
text(M, 104, "Manish Kumar", font="Sans-Bold", size=33, color=WHITE, cs=0.2)
nm_w = width_of("Manish Kumar", "Sans-Bold", 33, 0.2)
text(M + nm_w + 3, 104, ".", font="Sans-Bold", size=33, color=LIME)
rule(M, 116, M + 62, color=LIME, w=2.4)
text(M, 132, "Graphic & Visual Communication Designer", font="Sans-Light", size=13.5, color=BODY)

text(M, 158, "oflakstudio@gmail.com    ·    +91 97701 49478    ·    Janjgir-Champa, Chhattisgarh, India",
     font="Mono", size=8.1, color=GREY, cs=0.2)
text(M, 172, "linkedin.com/in/manish-kumar-5051023a9    ·    instagram.com/crea.graphix    ·    github.com/0flakstudio",
     font="Mono", size=8.1, color=GREY, cs=0.2)
rule(M, 186, PAGE_W - M)

# ============================ stats strip ================================
stats = [
    ("3+",   "YEARS"),
    ("25+",  "BRANDING PROJECTS"),
    ("500+", "CREATIVE ASSETS"),
    ("16+",  "BRANDS"),
    ("13",   "INDUSTRIES"),
]
n = len(stats); colw = CW / n
sy_num, sy_lab = 214, 228
for i, (num, lab) in enumerate(stats):
    cx = M + colw * i + colw / 2
    text(cx, sy_num, num, font="Sans-Bold", size=19, color=LIME, align="c")
    text(cx, sy_lab, lab, font="Mono", size=6.6, color=GREY, cs=1.1, align="c")
rule(M, 244, PAGE_W - M)

# ============================ columns ====================================
LX = M                      # left column x
LW = 168.0                  # left column width
RX = M + LW + 30            # right column x
RXR = PAGE_W - M            # right column right edge
top = 258

# ---- left surface panel -------------------------------------------------
c.setFillColor(SURFACE)
c.roundRect(LX - 10, T(PAGE_H - 44) , LW + 20, -(PAGE_H - 44 - (top - 14)), 10, stroke=0, fill=1) if False else None
# draw panel from top-14 down to just below the Strengths block
panel_top = top - 14
panel_bottom = 712
c.setFillColor(SURFACE)
c.roundRect(LX - 11, T(panel_bottom), LW + 22, (panel_bottom - panel_top), 11, stroke=0, fill=1)

# ---- LEFT: toolkit ------------------------------------------------------
ly = top
heading(LX, ly, "TOOLKIT")
ly += 16
toolkit = ["Adobe Photoshop, Illustrator,", "InDesign & Firefly", "Canva · WordPress",
           "Hostinger AI Website Builder", "AI creative workflows"]
for i, line in enumerate(toolkit):
    text(LX, ly, line, font="Sans", size=9.2, color=BODY)
    ly += 13.2

# ---- LEFT: selected work ------------------------------------------------
ly += 12
heading(LX, ly, "SELECTED WORK")
ly += 16
selected = [
    ("Feather Touch", "Beauty"),
    ("MKS India Fashion", "Fashion"),
    ("Agnitra Foundation", "NGO"),
    ("Automobile Villa", "Automotive"),
    ("Sai Agritech", "Agriculture"),
    ("Little Stars School", "Education"),
    ("Kanha Tofu", "Food & FMCG"),
    ("Dhaam App", "Astrology"),
]
for name, tag in selected:
    sq(LX, ly, s=3.4)
    text(LX + 9, ly, name, font="Sans-Bold", size=9.4, color=WHITE)
    nw = width_of(name, "Sans-Bold", 9.4)
    text(LX + 9 + nw + 7, ly, tag, font="Mono", size=6.9, color=GREY, cs=0.4)
    ly += 15.4

# ---- LEFT: education ----------------------------------------------------
ly += 11
heading(LX, ly, "EDUCATION")
ly += 16
text(LX, ly, "Certificate in Visual Arts —", font="Sans-Bold", size=9.3, color=WHITE); ly += 12
text(LX, ly, "Applied Arts (CVAA)", font="Sans-Bold", size=9.3, color=WHITE); ly += 12.5
text(LX, ly, "IGNOU, New Delhi · 2024", font="Mono", size=7.7, color=GREY); ly += 17
text(LX, ly, "Bachelor of Computer", font="Sans-Bold", size=9.3, color=WHITE); ly += 12
text(LX, ly, "Applications (BCA)", font="Sans-Bold", size=9.3, color=WHITE); ly += 12.5
text(LX, ly, "IGNOU, Ranchi · 2021–2023", font="Mono", size=7.7, color=GREY)

# ---- LEFT: strengths ----------------------------------------------------
ly += 26
heading(LX, ly, "STRENGTHS")
ly += 16
for s in ["Brand systems thinking", "Clear visual communication",
          "Fast, consistent delivery", "Cross-team collaboration"]:
    sq(LX, ly, s=3.4)
    text(LX + 9, ly, s, font="Sans", size=9.2, color=BODY)
    ly += 15.2

# ---- RIGHT: profile -----------------------------------------------------
ry = top
heading(RX, ry, "PROFILE", right=RXR)
ry += 16
profile = ("Graphic and visual communication designer and founder of Oflak Studio & Crea "
           "Graphix. Across 3+ years I have delivered 25+ branding projects for 16+ brands "
           "across a dozen-plus industries — healthcare, B2B technology, retail interiors, "
           "automotive, fashion & denim retail, agriculture, food & FMCG, wellness and NGO "
           "communication — pairing creative craft with clear, business-minded design.")
from reportlab.lib.utils import simpleSplit
for line in simpleSplit(profile, "Sans", 9.6, RXR - RX):
    text(RX, ry, line, font="Sans", size=9.6, color=BODY); ry += 13.1

# ---- RIGHT: experience --------------------------------------------------
ry += 9
heading(RX, ry, "EXPERIENCE", right=RXR)
ry += 18

def job(ry, role, period, org, bullets):
    text(RX, ry, role, font="Sans-Bold", size=11.2, color=WHITE)
    text(RXR, ry, period, font="Mono", size=8.0, color=LIME, cs=0.4, align="r")
    ry += 12.5
    text(RX, ry, org, font="Mono", size=8.1, color=GREY, cs=0.3)
    ry += 14
    for b in bullets:
        c.setFillColor(GREY); text(RX, ry, "—", font="Sans", size=9.4, color=GREY)
        for j, line in enumerate(simpleSplit(b, "Sans", 9.4, RXR - RX - 15)):
            text(RX + 15, ry, line, font="Sans", size=9.4, color=BODY); ry += 12.4
        ry += 1.0
    return ry + 5

ry = job(ry, "Digital Marketing Manager", "2024 – Present", "JGM Multispecialty Hospital",
         ["Design 100+ awareness posters, festival, doctor and recruitment creatives for a high-volume healthcare calendar.",
          "Built the hospital website (jgmhospital.com) with the Hostinger AI website builder.",
          "Supported a 40% improvement in patient outreach through digital campaign assets."])

ry = job(ry, "Graphic Designer Executive", "2023 – 2024", "Suprams Info Solutions, Delhi",
         ["Produced 300+ B2B technology creatives across print, digital, social, EDM, standees and brochures — for software, hardware, cloud and cybersecurity lines.",
          "Designed sales collateral featuring partner brands (Cisco, Sophos, Microsoft, AWS) and cut project turnaround by 25%."])

ry = job(ry, "Founder & Owner", "2023 – Present", "Oflak Studio & Crea Graphix · Independent",
         ["Delivered 25+ branding projects: identity systems, guidelines, marketing creatives and digital assets.",
          "Lifted client engagement by 35% through modernized digital assets and modular web design."])

# ---- RIGHT: certifications ---------------------------------------------
ry += 2
heading(RX, ry, "CERTIFICATIONS", right=RXR)
ry += 16
certs = [
    ("Digital Marketing Using AI", "Skill Nation · 2026"),
    ("UI/UX Design Mastery", "Beep · 2026"),
    ("AI Tools & Claude Workshop", "be10x · 2026"),
    ("Adobe Photoshop for Beginners", "Alison (CPD) · 2024"),
    ("Introduction to Graphic Design", "Alison (CPD) · 2024"),
    ("Retouching & Photo Editing", "JK Studios · 2024"),
    ("Canva Essentials", "Canva Design School · 2023"),
    ("Graphic Design Essentials", "Canva Design School · 2023"),
]
col2x = RX + (RXR - RX) / 2 + 6
rowh = 23
for i, (title, meta) in enumerate(certs):
    cx = RX if i % 2 == 0 else col2x
    if i % 2 == 0 and i > 0:
        ry += rowh
    yy = ry
    sq(cx, yy, s=3.4)
    text(cx + 9, yy, title, font="Sans-Bold", size=8.7, color=WHITE)
    text(cx + 9, yy + 11, meta, font="Mono", size=6.8, color=GREY, cs=0.2)

# ============================ footer =====================================
rule(M, PAGE_H - 48, PAGE_W - M)
text(M, PAGE_H - 36, "MANISH KUMAR · CREA GRAPHIX", font="Mono", size=7.4, color=GREY, cs=1.0)
text(PAGE_W - M, PAGE_H - 36, "Creativity. Simplified.", font="Mono", size=7.4, color=GREY, cs=0.6, align="r")

c.showPage()
c.save()
print("CV written to outputs/Manish-Kumar-CV.pdf")
