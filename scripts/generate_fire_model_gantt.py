from __future__ import annotations

import struct
import zlib
from pathlib import Path
from xml.sax.saxutils import escape

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

WIDTH = 1800
HEIGHT = 1120
MARGIN_LEFT = 350
MARGIN_RIGHT = 90
MARGIN_TOP = 150
MARGIN_BOTTOM = 180
CHART_WIDTH = WIDTH - MARGIN_LEFT - MARGIN_RIGHT
CHART_HEIGHT = HEIGHT - MARGIN_TOP - MARGIN_BOTTOM
TOTAL_MONTHS = 36
ROW_HEIGHT = 52
BAR_HEIGHT = 30
MONTH_WIDTH = CHART_WIDTH / TOTAL_MONTHS

PHASES = [
    {"label": "Setup", "start": 1, "end": 6, "color": "#f7efe3"},
    {"label": "Measure", "start": 7, "end": 18, "color": "#eef6ea"},
    {"label": "Test", "start": 19, "end": 30, "color": "#eef3f9"},
    {"label": "Apply", "start": 31, "end": 36, "color": "#f5eef9"},
]

ROLE_COLORS = {
    "PI": "#2b6cb0",
    "Postdoc 1": "#2f855a",
    "Postdoc 2": "#2c7a7b",
    "Shared": "#7b8794",
}

TASKS = [
    ("Team and workflow setup", 1, 4, "Shared"),
    ("Data governance and infrastructure", 2, 6, "PI"),
    ("Wildfire trajectory assembly", 3, 12, "Postdoc 1"),
    ("QA/QC and provenance checks", 5, 10, "Postdoc 1"),
    ("Scaling diagnostics v1", 7, 9, "Postdoc 1"),
    ("Minimal model hierarchy", 4, 10, "Postdoc 2"),
    ("Shared observables and metadata", 6, 8, "PI"),
    ("Regime detection and collapse tests", 13, 10, "Postdoc 1"),
    ("Parameter sweeps and ablation tests", 14, 12, "Postdoc 2"),
    ("Phase diagram synthesis", 20, 8, "PI"),
    ("Empirical + generative integration", 19, 10, "PI"),
    ("Benchmarking existing fire models", 25, 9, "PI"),
    ("Toolkit, data, and code release", 28, 8, "Shared"),
    ("Synthesis papers and reporting", 30, 7, "Shared"),
]

GROUPS = [
    ("Team and workflow setup", 0, 1),
    ("Empirical data and diagnostics", 2, 4),
    ("Generative modeling", 5, 5),
    ("Integration and evaluation", 6, 11),
    ("Outputs and dissemination", 12, 13),
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
        color = hex_to_rgb(background)
        self.pixels = bytearray(color * width * height)

    def fill_rect(self, x: int, y: int, w: int, h: int, color: str) -> None:
        rgb = hex_to_rgb(color)
        x0 = max(0, x)
        y0 = max(0, y)
        x1 = min(self.width, x + w)
        y1 = min(self.height, y + h)
        if x0 >= x1 or y0 >= y1:
            return
        for yy in range(y0, y1):
            row = yy * self.width * 3
            for xx in range(x0, x1):
                idx = row + xx * 3
                self.pixels[idx:idx + 3] = rgb

    def line(self, x0: int, y0: int, x1: int, y1: int, color: str, thickness: int = 1) -> None:
        if x0 == x1:
            self.fill_rect(x0 - thickness // 2, min(y0, y1), thickness, abs(y1 - y0) + 1, color)
            return
        if y0 == y1:
            self.fill_rect(min(x0, x1), y0 - thickness // 2, abs(x1 - x0) + 1, thickness, color)
            return
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while True:
            self.fill_rect(x0 - thickness // 2, y0 - thickness // 2, thickness, thickness, color)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def text(self, x: int, y: int, text: str, color: str, scale: int = 2) -> None:
        cursor_x = x
        for char in text.upper():
            glyph = FONT.get(char, FONT[" "])
            for row_idx, row in enumerate(glyph):
                for col_idx, bit in enumerate(row):
                    if bit == "1":
                        self.fill_rect(cursor_x + col_idx * scale, y + row_idx * scale, scale, scale, color)
            cursor_x += (len(glyph[0]) + 1) * scale

    def save(self, path: Path) -> None:
        raw = bytearray()
        stride = self.width * 3
        for y in range(self.height):
            raw.append(0)
            start = y * stride
            raw.extend(self.pixels[start:start + stride])
        compressed = zlib.compress(bytes(raw), level=9)
        png = bytearray(b"\x89PNG\r\n\x1a\n")
        png.extend(chunk(b"IHDR", struct.pack(">IIBBBBB", self.width, self.height, 8, 2, 0, 0, 0)))
        png.extend(chunk(b"IDAT", compressed))
        png.extend(chunk(b"IEND", b""))
        path.write_bytes(png)


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
            f'<text x="{x:.2f}" y="{y:.2f}" fill="{fill}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(text)}</text>'
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



def draw_common(svg: SVGCanvas | None = None, png: PNGCanvas | None = None) -> None:
    total_rows = len(TASKS)
    chart_bottom = MARGIN_TOP + total_rows * ROW_HEIGHT

    for phase in PHASES:
        x = month_to_x(phase["start"])
        w = (phase["end"] - phase["start"] + 1) * MONTH_WIDTH
        if svg:
            svg.rect(x, MARGIN_TOP - 10, w, total_rows * ROW_HEIGHT + 20, phase["color"])
            svg.text(x + 10, MARGIN_TOP - 20, phase["label"], "#4a5568", 22, "700")
        if png:
            png.fill_rect(round(x), MARGIN_TOP - 10, round(w), total_rows * ROW_HEIGHT + 20, phase["color"])
            png.text(round(x) + 10, MARGIN_TOP - 48, phase["label"], "#4a5568", scale=3)

    for month in range(1, TOTAL_MONTHS + 1):
        x = month_to_x(month)
        if svg:
            svg.line(x, MARGIN_TOP, x, chart_bottom, "#d9e2ec", 1)
            svg.text(x + MONTH_WIDTH / 2, chart_bottom + 26, str(month), "#4a5568", 12, anchor="middle")
        if png:
            png.line(round(x), MARGIN_TOP, round(x), round(chart_bottom), "#d9e2ec", 1)
            png.text(round(x + MONTH_WIDTH / 2) - 8, round(chart_bottom) + 18, str(month), "#4a5568", scale=2)

    for year_end in (12, 24, 36):
        x = month_to_x(year_end + 1)
        if svg:
            svg.line(x, MARGIN_TOP - 10, x, chart_bottom, "#b9c6d3", 2)
        if png:
            png.line(round(x), MARGIN_TOP - 10, round(x), round(chart_bottom), "#b9c6d3", 2)

    year_specs = [(1, 12, "Year 1"), (13, 24, "Year 2"), (25, 36, "Year 3")]
    for start, end, label in year_specs:
        center = (month_to_x(start) + month_to_x(end + 1)) / 2
        if svg:
            svg.text(center, MARGIN_TOP - 48, label, "#2d3748", 22, "700", "middle")
        if png:
            png.text(round(center) - 38, MARGIN_TOP - 90, label, "#2d3748", scale=3)

    for group_name, start_idx, end_idx in GROUPS:
        y = MARGIN_TOP + ((start_idx + end_idx + 1) / 2) * ROW_HEIGHT
        divider_y = MARGIN_TOP + (end_idx + 1) * ROW_HEIGHT
        if svg:
            svg.text(MARGIN_LEFT - 24, y, group_name, "#2d3748", 18, "700", "end")
            svg.line(MARGIN_LEFT, divider_y, WIDTH - MARGIN_RIGHT, divider_y, "#d6dde5", 1.5)
        if png:
            png.text(20, round(y) - 12, group_name, "#2d3748", scale=2)
            png.line(MARGIN_LEFT, round(divider_y), WIDTH - MARGIN_RIGHT, round(divider_y), "#d6dde5", 1)

    for row, (label, start, duration, role) in enumerate(TASKS):
        x = month_to_x(start) + 6
        y = row_to_y(row) + (ROW_HEIGHT - BAR_HEIGHT) / 2
        w = duration * MONTH_WIDTH - 12
        color = ROLE_COLORS[role]
        if svg:
            svg.rect(x, y, w, BAR_HEIGHT, color, stroke="#ffffff", stroke_width=1.5, rx=8)
            svg.text(x + 10, y + 21, label, "#ffffff", 14, "700")
        if png:
            png.fill_rect(round(x), round(y), round(w), BAR_HEIGHT, color)
            png.text(round(x) + 8, round(y) + 8, label[: max(1, int((w - 16) // 12))], "#ffffff", scale=2)

    title = "FIRE-MODEL Work Plan Gantt Chart"
    subtitle = "ESIIL-style planning view linking roles, benchmarks, and deliverables across a 36-month project."
    if svg:
        svg.text(MARGIN_LEFT - 10, 56, title, "#1a202c", 36, "700")
        svg.text(MARGIN_LEFT - 10, 92, subtitle, "#4a5568", 18)
        svg.text((MARGIN_LEFT + WIDTH - MARGIN_RIGHT) / 2, HEIGHT - 38, "Project month", "#2d3748", 18, "700", "middle")
    if png:
        png.text(MARGIN_LEFT - 8, 36, title, "#1a202c", scale=4)
        png.text(MARGIN_LEFT - 8, 82, subtitle, "#4a5568", scale=2)
        png.text(WIDTH // 2 - 70, HEIGHT - 58, "Project month", "#2d3748", scale=3)

    legend_items = list(ROLE_COLORS.items()) + [(f"Benchmark: {phase['label']}", phase["color"]) for phase in PHASES]
    legend_x = MARGIN_LEFT
    legend_y = HEIGHT - 112
    for idx, (label, color) in enumerate(legend_items):
        x = legend_x + (idx % 4) * 350
        y = legend_y + (idx // 4) * 42
        if svg:
            svg.rect(x, y, 24, 24, color, stroke="#cbd5e0", stroke_width=0.8, rx=3)
            svg.text(x + 34, y + 18, label, "#2d3748", 15)
        if png:
            png.fill_rect(x, y, 24, 24, color)
            png.text(x + 34, y + 6, label, "#2d3748", scale=2)



def render_with_matplotlib() -> None:
    fig, ax = plt.subplots(figsize=(16, 9))
    total_rows = len(TASKS)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    for phase in PHASES:
        width = phase["end"] - phase["start"] + 1
        ax.add_patch(Rectangle((phase["start"] - 0.5, -0.5), width, total_rows, facecolor=phase["color"], edgecolor="none", zorder=0))
        ax.text(phase["start"] - 0.2, -0.9, phase["label"], fontsize=11, fontweight="bold", color="#4a5568", va="top")

    for row, (label, start, duration, role) in enumerate(TASKS):
        ax.barh(row, duration, left=start - 0.5, height=0.62, color=ROLE_COLORS[role], edgecolor="white", linewidth=1.0, zorder=3)
        ax.text(start - 0.2, row, label, ha="left", va="center", fontsize=9.5, color="white", zorder=4)

    ax.set_xlim(-6.0, 36.5)
    ax.set_ylim(-1.2, total_rows - 0.4)
    ax.set_yticks(range(total_rows))
    ax.set_yticklabels([""] * total_rows)
    ax.invert_yaxis()
    ax.set_xticks(range(1, 37))
    ax.set_xticklabels([str(i) for i in range(1, 37)], fontsize=9)
    ax.grid(axis="x", color="#d9e2ec", linewidth=0.8, alpha=0.9)
    ax.set_axisbelow(True)

    for year_start, year_end, label in [(1, 12, "Year 1"), (13, 24, "Year 2"), (25, 36, "Year 3")]:
        center = (year_start + year_end) / 2
        ax.text(center, -1.05, label, ha="center", va="bottom", fontsize=11, fontweight="bold", color="#2d3748")
        ax.vlines(year_end + 0.5, -0.5, total_rows - 0.4, color="#b9c6d3", linewidth=1.2, zorder=2)

    for group_name, start_idx, end_idx in GROUPS:
        center = (start_idx + end_idx) / 2
        ax.text(-5.2, center, group_name, ha="right", va="center", fontsize=10, fontweight="bold", color="#2d3748")
        ax.hlines(end_idx + 0.5, 0.5, 36.5, color="#d6dde5", linewidth=1.1, zorder=1)

    ax.set_title("FIRE-MODEL Work Plan Gantt Chart", fontsize=20, fontweight="bold", loc="left", pad=22)
    ax.text(-5.95, -1.85, "ESIIL-style planning view linking roles, benchmarks, and deliverables across a 36-month project.", fontsize=10.5, color="#4a5568", ha="left", va="bottom")
    ax.set_xlabel("Project month", fontsize=11, fontweight="bold", color="#2d3748", labelpad=12)

    legend_handles = [Patch(facecolor=color, edgecolor="none", label=label) for label, color in ROLE_COLORS.items()]
    phase_handles = [Patch(facecolor=phase["color"], edgecolor="none", label=f"Benchmark: {phase['label']}") for phase in PHASES]
    ax.legend(handles=legend_handles + phase_handles, ncol=4, frameon=False, fontsize=9, loc="lower left", bbox_to_anchor=(0.0, -0.22))

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
