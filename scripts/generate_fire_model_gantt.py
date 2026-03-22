from __future__ import annotations

import struct
import zlib
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont

try:  # Optional dependency path.
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch, Rectangle
except ModuleNotFoundError:  # Pure-Python fallback keeps the script runnable.
    plt = None
    Patch = None
    Rectangle = None


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "docs" / "assets" / "figures"
PNG_PATH = OUTPUT_DIR / "fire_model_gantt_ESIIL_minimal.png"
SVG_PATH = OUTPUT_DIR / "fire_model_gantt_ESIIL_minimal.svg"
# The SVG is repository-friendly for review and site rendering; the workflow also regenerates
# both SVG and PNG inside GitHub so binary artifacts do not need to be attached to code review.

WIDTH = 2440
HEIGHT = 1820
MARGIN_LEFT = 860
MARGIN_RIGHT = 100
MARGIN_TOP = 270
MARGIN_BOTTOM = 240
CHART_WIDTH = WIDTH - MARGIN_LEFT - MARGIN_RIGHT
CHART_HEIGHT = HEIGHT - MARGIN_TOP - MARGIN_BOTTOM
TOTAL_MONTHS = 36
ROW_HEIGHT = 42
BAR_HEIGHT = 18
MONTH_WIDTH = CHART_WIDTH / TOTAL_MONTHS

STAGE_BANDS = [
    {"label": "Pipeline + reliability", "start": 1, "end": 6, "color": "#f7efe3"},
    {"label": "Observables + Benchmark 0", "start": 7, "end": 12, "color": "#eef6ea"},
    {"label": "Model contrasts", "start": 13, "end": 18, "color": "#eef3f9"},
    {"label": "Validation + sufficiency", "start": 19, "end": 24, "color": "#eef1fb"},
    {"label": "Packaging + user testing", "start": 25, "end": 30, "color": "#f4effa"},
    {"label": "Release + transfer", "start": 31, "end": 36, "color": "#fbf1f4"},
]

ROLE_COLORS = {
    "PI": "#2b6cb0",
    "Postdoc 1": "#2f855a",
    "Postdoc 2": "#2c7a7b",
    "Shared": "#7b8794",
}

GROUP_ORDER = [
    "Team and workflow setup",
    "Empirical data and diagnostics",
    "Generative modeling",
    "Integration and evaluation",
    "Outputs and dissemination",
]

GROUP_DISPLAY = {
    "Team and workflow setup": "Team / workflow",
    "Empirical data and diagnostics": "Empirical diagnostics",
    "Generative modeling": "Generative modeling",
    "Integration and evaluation": "Integration / evaluation",
    "Outputs and dissemination": "Outputs / dissemination",
}

FONT_REGULAR_PATH = Path("/System/Library/Fonts/Supplemental/Times New Roman.ttf")
FONT_BOLD_PATH = Path("/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf")
FONT_STACK = "Times New Roman, Georgia, serif"

TASKS = [
    {"label": "Team and workflow setup", "start": 1, "end": 3, "role": "Shared", "group": "Team and workflow setup"},
    {"label": "Data governance and infrastructure", "start": 1, "end": 4, "role": "PI", "group": "Team and workflow setup"},
    {"label": "Event catalog stabilization", "start": 2, "end": 5, "role": "Postdoc 1", "group": "Empirical data and diagnostics"},
    {"label": "Wildfire trajectory assembly", "start": 3, "end": 7, "role": "Postdoc 1", "group": "Empirical data and diagnostics"},
    {"label": "QA/QC and provenance checks", "start": 4, "end": 8, "role": "Postdoc 1", "group": "Empirical data and diagnostics"},
    {"label": "Metric-definition freeze", "start": 7, "end": 9, "role": "Shared", "group": "Empirical data and diagnostics"},
    {"label": "Scaling diagnostics v1", "start": 7, "end": 10, "role": "Postdoc 1", "group": "Empirical data and diagnostics"},
    {"label": "Shared observables and metadata", "start": 8, "end": 11, "role": "Shared", "group": "Empirical data and diagnostics"},
    {"label": "Cross-region replication", "start": 10, "end": 12, "role": "Postdoc 1", "group": "Empirical data and diagnostics"},
    {"label": "Initial comparison engine", "start": 8, "end": 12, "role": "Postdoc 2", "group": "Generative modeling"},
    {"label": "Model library v1", "start": 13, "end": 16, "role": "Postdoc 2", "group": "Generative modeling"},
    {"label": "Controlled model contrasts (M0-M3)", "start": 15, "end": 20, "role": "Postdoc 2", "group": "Generative modeling"},
    {"label": "Ablation experiments", "start": 17, "end": 21, "role": "Postdoc 2", "group": "Generative modeling"},
    {"label": "Parameter sweeps", "start": 16, "end": 21, "role": "Postdoc 2", "group": "Generative modeling"},
    {"label": "Benchmark 0", "start": 10, "end": 12, "role": "Shared", "group": "Integration and evaluation", "gate": True},
    {"label": "Regime detection and transition testing", "start": 13, "end": 18, "role": "Shared", "group": "Integration and evaluation"},
    {"label": "Calibration audits across regimes", "start": 18, "end": 23, "role": "PI", "group": "Integration and evaluation"},
    {"label": "Validation framework v1", "start": 19, "end": 24, "role": "Shared", "group": "Integration and evaluation"},
    {"label": "Phase diagram synthesis", "start": 20, "end": 24, "role": "PI", "group": "Integration and evaluation"},
    {"label": "Publication-ready comparison figures", "start": 21, "end": 24, "role": "Shared", "group": "Integration and evaluation"},
    {"label": "Evidence-weighted sufficiency maps", "start": 22, "end": 24, "role": "PI", "group": "Integration and evaluation"},
    {"label": "Empirical + generative integration", "start": 25, "end": 29, "role": "PI", "group": "Integration and evaluation"},
    {"label": "Benchmarking existing and future fire models", "start": 25, "end": 31, "role": "Shared", "group": "Integration and evaluation"},
    {"label": "External user testing", "start": 28, "end": 32, "role": "Shared", "group": "Integration and evaluation"},
    {"label": "Final uncertainty-reporting templates", "start": 27, "end": 31, "role": "PI", "group": "Integration and evaluation"},
    {"label": "Benchmark release engineering", "start": 29, "end": 34, "role": "Shared", "group": "Outputs and dissemination"},
    {"label": "Public release readiness", "start": 31, "end": 34, "role": "Shared", "group": "Outputs and dissemination"},
    {"label": "Toolkit, data, and code release", "start": 33, "end": 36, "role": "Shared", "group": "Outputs and dissemination"},
    {"label": "Onboarding and support", "start": 33, "end": 36, "role": "Shared", "group": "Outputs and dissemination"},
    {"label": "Transfer / handoff materials", "start": 34, "end": 36, "role": "PI", "group": "Outputs and dissemination"},
    {"label": "Evidence book and mechanism synthesis", "start": 30, "end": 36, "role": "PI", "group": "Outputs and dissemination"},
    {"label": "Synthesis papers and reporting", "start": 31, "end": 36, "role": "Shared", "group": "Outputs and dissemination"},
]

FONT = {
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    "/": ["00001", "00010", "00100", "01000", "10000", "00000", "00000"],
    ":": ["00000", "00100", "00100", "00000", "00100", "00100", "00000"],
    ".": ["00000", "00000", "00000", "00000", "00000", "00110", "00110"],
    ",": ["00000", "00000", "00000", "00000", "00110", "00110", "00100"],
    "+": ["00000", "00100", "00100", "11111", "00100", "00100", "00000"],
    "(": ["00010", "00100", "01000", "01000", "01000", "00100", "00010"],
    ")": ["01000", "00100", "00010", "00010", "00010", "00100", "01000"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11111", "10000", "10000", "11110", "00001", "00001", "11110"],
    "6": ["01110", "10000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00001", "01110"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01111", "10000", "10000", "10111", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["01110", "00100", "00100", "00100", "00100", "00100", "01110"],
    "J": ["00001", "00001", "00001", "00001", "10001", "10001", "01110"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
}


class PNGCanvas:
    def __init__(self, width: int, height: int, background: str = "#ffffff") -> None:
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height), background)
        self.draw = ImageDraw.Draw(self.image)

    def _font(self, size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
        try:
            path = FONT_BOLD_PATH if bold else FONT_REGULAR_PATH
            return ImageFont.truetype(str(path), size=size)
        except OSError:
            return ImageFont.load_default()

    def fill_rect(self, x: int, y: int, w: int, h: int, color: str) -> None:
        if w <= 0 or h <= 0:
            return
        self.draw.rectangle([x, y, x + w, y + h], fill=color)

    def line(self, x0: int, y0: int, x1: int, y1: int, color: str, thickness: int = 1) -> None:
        self.draw.line([(x0, y0), (x1, y1)], fill=color, width=thickness)

    def rounded_rect(self, x: int, y: int, w: int, h: int, fill: str, outline: str | None = None, outline_width: int = 1, radius: int = 8) -> None:
        self.draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=fill, outline=outline, width=outline_width)

    def text(self, x: int, y: int, text: str, color: str, size: int = 16, bold: bool = False, anchor: str = "la") -> None:
        self.draw.text((x, y), text, fill=color, font=self._font(size=size, bold=bold), anchor=anchor)

    def save(self, path: Path) -> None:
        self.image.save(path, format="PNG")


class SVGCanvas:
    def __init__(self, width: int, height: int, background: str = "#ffffff") -> None:
        self.width = width
        self.height = height
        self.elements = [f'<rect width="100%" height="100%" fill="{background}"/>']

    def rect(self, x: float, y: float, w: float, h: float, fill: str, stroke: str = "none", stroke_width: float = 0, rx: float = 0) -> None:
        self.elements.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" rx="{rx}"/>'
        )

    def line(self, x1: float, y1: float, x2: float, y2: float, stroke: str, stroke_width: float = 1) -> None:
        self.elements.append(
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
        )

    def text(self, x: float, y: float, text: str, fill: str, size: int, weight: str = "400", anchor: str = "start") -> None:
        self.elements.append(
            f'<text x="{x:.2f}" y="{y:.2f}" fill="{fill}" font-family="{FONT_STACK}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(text)}</text>'
        )

    def save(self, path: Path) -> None:
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">'
            + "".join(self.elements)
            + "</svg>"
        )
        path.write_text(svg)



def chunk(tag: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)



def hex_to_rgb(value: str) -> bytes:
    value = value.lstrip("#")
    return bytes(int(value[i:i + 2], 16) for i in (0, 2, 4))



def month_to_x(month: float) -> float:
    return MARGIN_LEFT + (month - 1) * MONTH_WIDTH



def row_to_y(row: int) -> float:
    return MARGIN_TOP + row * ROW_HEIGHT



def task_duration(task: dict[str, object]) -> int:
    return int(task["end"]) - int(task["start"]) + 1



def group_bounds() -> list[tuple[str, int, int]]:
    bounds: list[tuple[str, int, int]] = []
    for group in GROUP_ORDER:
        indices = [idx for idx, task in enumerate(TASKS) if task["group"] == group]
        if indices:
            bounds.append((group, min(indices), max(indices)))
    return bounds



def draw_common(svg: SVGCanvas | None = None, png: PNGCanvas | None = None) -> None:
    total_rows = len(TASKS)
    chart_bottom = MARGIN_TOP + total_rows * ROW_HEIGHT

    for band in STAGE_BANDS:
        x = month_to_x(band["start"])
        w = (band["end"] - band["start"] + 1) * MONTH_WIDTH
        if svg:
            svg.rect(x, MARGIN_TOP - 10, w, total_rows * ROW_HEIGHT + 20, band["color"])
            svg.text(x + 10, MARGIN_TOP - 34, band["label"], "#4a5568", 13, "700")
        if png:
            png.fill_rect(round(x), MARGIN_TOP - 10, round(w), total_rows * ROW_HEIGHT + 20, band["color"])
            png.text(round(x) + 10, MARGIN_TOP - 56, band["label"], "#4a5568", size=18, bold=True)

    for month in range(1, TOTAL_MONTHS + 1):
        x = month_to_x(month)
        quarter_line = month == 1 or (month - 1) % 3 == 0
        stroke = "#c3d0dc" if quarter_line else "#d9e2ec"
        width = 1.6 if quarter_line else 1
        if svg:
            svg.line(x, MARGIN_TOP, x, chart_bottom, stroke, width)
            svg.text(x + MONTH_WIDTH / 2, chart_bottom + 26, str(month), "#4a5568", 12, anchor="middle")
        if png:
            png.line(round(x), MARGIN_TOP, round(x), round(chart_bottom), stroke, 1 if not quarter_line else 2)
            png.text(round(x + MONTH_WIDTH / 2), round(chart_bottom) + 26, str(month), "#4a5568", size=16, anchor="ma")

    for year_end in (12, 24, 36):
        x = month_to_x(year_end + 1)
        if svg:
            svg.line(x, MARGIN_TOP - 10, x, chart_bottom, "#b9c6d3", 2)
        if png:
            png.line(round(x), MARGIN_TOP - 10, round(x), round(chart_bottom), "#b9c6d3", 2)

    year_specs = [
        (1, 12, "Year 1 - Detect"),
        (13, 24, "Year 2 - Explain"),
        (25, 36, "Year 3 - Apply"),
    ]
    for start, end, label in year_specs:
        center = (month_to_x(start) + month_to_x(end + 1)) / 2
        if svg:
            svg.text(center, MARGIN_TOP - 86, label, "#2d3748", 24, "700", "middle")
        if png:
            png.text(round(center), MARGIN_TOP - 104, label, "#2d3748", size=28, bold=True, anchor="ma")

    for group_name, start_idx, end_idx in group_bounds():
        y = MARGIN_TOP + ((start_idx + end_idx + 1) / 2) * ROW_HEIGHT
        divider_y = MARGIN_TOP + (end_idx + 1) * ROW_HEIGHT
        group_label = GROUP_DISPLAY[group_name]
        if svg:
            svg.text(48, y, group_label, "#2d3748", 15, "700", "start")
            svg.line(MARGIN_LEFT, divider_y, WIDTH - MARGIN_RIGHT, divider_y, "#d6dde5", 1.5)
        if png:
            png.text(48, round(y), group_label, "#2d3748", size=20, bold=True, anchor="lm")
            png.line(MARGIN_LEFT, round(divider_y), WIDTH - MARGIN_RIGHT, round(divider_y), "#d6dde5", 1)

    for row, task in enumerate(TASKS):
        label = str(task["label"])
        start = int(task["start"])
        end = int(task["end"])
        role = str(task["role"])
        x = month_to_x(start) + 6
        y = row_to_y(row) + (ROW_HEIGHT - BAR_HEIGHT) / 2
        bar_height = BAR_HEIGHT + (4 if task.get("gate") else 0)
        y -= (bar_height - BAR_HEIGHT) / 2
        w = task_duration(task) * MONTH_WIDTH - 12
        color = ROLE_COLORS[role]
        stroke = "#8b5e34" if task.get("gate") else "#ffffff"
        stroke_width = 2.4 if task.get("gate") else 1.0
        if svg:
            svg.text(MARGIN_LEFT - 18, y + bar_height * 0.72, label, "#243b53", 14, "400", "end")
            svg.rect(x, y, w, bar_height, color, stroke=stroke, stroke_width=stroke_width, rx=8)
        if png:
            png.text(MARGIN_LEFT - 18, round(y + bar_height * 0.7), label, "#243b53", size=18, anchor="rm")
            png.rounded_rect(round(x), round(y), round(w), round(bar_height), color, outline=stroke if task.get("gate") else "#ffffff", outline_width=2 if task.get("gate") else 1, radius=8)
            if task.get("gate"):
                png.line(round(x), round(y), round(x + w), round(y), stroke, 2)
                png.line(round(x), round(y + bar_height), round(x + w), round(y + bar_height), stroke, 2)
                png.line(round(x), round(y), round(x), round(y + bar_height), stroke, 2)
                png.line(round(x + w), round(y), round(x + w), round(y + bar_height), stroke, 2)

    title = "FIRE-MODEL Work Plan Gantt Chart"
    subtitle = "Decision-gated 36-month plan aligning Detect, Explain, and Apply workstreams with roles, benchmarks, and deliverables."
    if svg:
        svg.text(MARGIN_LEFT - 10, 56, title, "#1a202c", 36, "700")
        svg.text(MARGIN_LEFT - 10, 92, subtitle, "#4a5568", 18)
        svg.text((MARGIN_LEFT + WIDTH - MARGIN_RIGHT) / 2, HEIGHT - 38, "Project month", "#2d3748", 18, "700", "middle")
    if png:
        png.text(MARGIN_LEFT - 8, 54, title, "#1a202c", size=44, bold=True)
        png.text(MARGIN_LEFT - 8, 98, subtitle, "#4a5568", size=20)
        png.text(WIDTH // 2, HEIGHT - 64, "Project month", "#2d3748", size=28, bold=True, anchor="ma")

    legend_items = [{"label": label, "fill": color, "stroke": "none", "stroke_width": 0.8} for label, color in ROLE_COLORS.items()]
    legend_items.append({"label": "Benchmark 0 gate", "fill": ROLE_COLORS["Shared"], "stroke": "#8b5e34", "stroke_width": 2.2})
    legend_x = MARGIN_LEFT
    legend_y = HEIGHT - 112
    for idx, item in enumerate(legend_items):
        x = legend_x + (idx % 3) * 360
        y = legend_y + (idx // 3) * 42
        if svg:
            svg.rect(x, y, 24, 24, item["fill"], stroke=item["stroke"], stroke_width=item["stroke_width"], rx=3)
            svg.text(x + 34, y + 18, str(item["label"]), "#2d3748", 15)
        if png:
            png.rounded_rect(x, y, 24, 24, str(item["fill"]), outline=None if item["stroke"] == "none" else str(item["stroke"]), outline_width=2 if item["stroke"] != "none" else 1, radius=3)
            png.text(x + 34, y + 16, str(item["label"]), "#2d3748", size=18, anchor="lm")



def render_with_matplotlib() -> None:
    fig, ax = plt.subplots(figsize=(18.5, 12))
    total_rows = len(TASKS)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    for band in STAGE_BANDS:
        width = band["end"] - band["start"] + 1
        ax.add_patch(Rectangle((band["start"] - 0.5, -0.5), width, total_rows, facecolor=band["color"], edgecolor="none", zorder=0))
        ax.text(band["start"] - 0.25, -0.95, band["label"], fontsize=9.5, fontweight="bold", color="#4a5568", va="top")

    for row, task in enumerate(TASKS):
        label = str(task["label"])
        start = int(task["start"])
        duration = task_duration(task)
        role = str(task["role"])
        edgecolor = "#8b5e34" if task.get("gate") else "white"
        linewidth = 2.2 if task.get("gate") else 1.0
        height = 0.74 if task.get("gate") else 0.56
        ax.barh(row, duration, left=start - 0.5, height=height, color=ROLE_COLORS[role], edgecolor=edgecolor, linewidth=linewidth, zorder=3)
        ax.text(-0.85, row, label, ha="right", va="center", fontsize=9.6, color="#243b53", zorder=4)

    ax.set_xlim(-8.6, 36.5)
    ax.set_ylim(-1.2, total_rows - 0.4)
    ax.set_yticks(range(total_rows))
    ax.set_yticklabels([""] * total_rows)
    ax.invert_yaxis()
    ax.set_xticks(range(1, 37))
    ax.set_xticklabels([str(i) for i in range(1, 37)], fontsize=9)
    ax.grid(axis="x", color="#d9e2ec", linewidth=0.7, alpha=0.95)
    ax.set_axisbelow(True)
    for quarter_start in (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34):
        ax.vlines(quarter_start - 0.5, -0.5, total_rows - 0.4, color="#c3d0dc", linewidth=1.2, zorder=1)

    for year_start, year_end, label in [
        (1, 12, "Year 1 - Detect"),
        (13, 24, "Year 2 - Explain"),
        (25, 36, "Year 3 - Apply"),
    ]:
        center = (year_start + year_end) / 2
        ax.text(center, -1.2, label, ha="center", va="bottom", fontsize=12.5, fontweight="bold", color="#2d3748")
        ax.vlines(year_end + 0.5, -0.5, total_rows - 0.4, color="#b9c6d3", linewidth=1.2, zorder=2)

    for group_name, start_idx, end_idx in group_bounds():
        center = (start_idx + end_idx) / 2
        ax.text(-7.9, center, group_name, ha="left", va="center", fontsize=10.3, fontweight="bold", color="#2d3748")
        ax.hlines(end_idx + 0.5, 0.5, 36.5, color="#d6dde5", linewidth=1.1, zorder=1)

    ax.set_title("FIRE-MODEL Work Plan Gantt Chart", fontsize=20, fontweight="bold", loc="left", pad=22)
    ax.text(-8.45, -1.88, "Decision-gated 36-month plan aligning Detect, Explain, and Apply workstreams with roles, benchmarks, and deliverables.", fontsize=10.2, color="#4a5568", ha="left", va="bottom")
    ax.set_xlabel("Project month", fontsize=11, fontweight="bold", color="#2d3748", labelpad=12)

    legend_handles = [Patch(facecolor=color, edgecolor="none", label=label) for label, color in ROLE_COLORS.items()]
    legend_handles.append(Patch(facecolor=ROLE_COLORS["Shared"], edgecolor="#8b5e34", linewidth=2.0, label="Benchmark 0 gate"))
    ax.legend(handles=legend_handles, ncol=3, frameon=False, fontsize=9.5, loc="lower left", bbox_to_anchor=(0.0, -0.2))

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", colors="#4a5568")
    plt.tight_layout()
    fig.savefig(PNG_PATH, dpi=300, bbox_inches="tight")
    fig.savefig(SVG_PATH, bbox_inches="tight")
    plt.close(fig)



def render_pure_python() -> None:
    png = PNGCanvas(WIDTH, HEIGHT)
    svg = SVGCanvas(WIDTH, HEIGHT)
    draw_common(svg=svg, png=png)
    svg.save(SVG_PATH)
    png.save(PNG_PATH)



def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if plt is not None:
        render_with_matplotlib()
        mode = "matplotlib"
    else:
        render_pure_python()
        mode = "pure-python fallback"
    print(f"Saved {PNG_PATH}")
    print(f"Saved {SVG_PATH}")
    print(f"Renderer: {mode}")


if __name__ == "__main__":
    main()
