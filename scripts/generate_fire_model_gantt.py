from __future__ import annotations

"""Generate the proposal-ready FIRE-MODEL Gantt chart.

Default behavior is dependency-free (pure-Python SVG generation) so CI can run
without Matplotlib. Optional PNG/PDF export is available with --all-formats when
Matplotlib is installed.

Readability update (2026-04-07):
- increased row/category spacing and margins for proposal-scale legibility,
- shortened task/milestone wording to match current Verify/Predict/Synthesis language,
- moved milestone labels into a staggered right-side annotation column with leader lines.
"""

import argparse
from pathlib import Path
from xml.sax.saxutils import escape

try:
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
except ModuleNotFoundError:
    plt = None
    Line2D = None

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "docs" / "assets" / "figures"
BASENAME = "fire_model_gantt_verify_predict_synthesis"
PNG_PATH = OUTPUT_DIR / f"{BASENAME}.png"
PDF_PATH = OUTPUT_DIR / f"{BASENAME}.pdf"
SVG_PATH = OUTPUT_DIR / f"{BASENAME}.svg"

TOTAL_MONTHS = 36
ROW_STEP = 1.55
GROUP_GAP = 1.6

PHASES = [
    {"start": 1, "end": 12, "label": "Year 1 — Verify", "shade": "#f5f7fb"},
    {"start": 13, "end": 24, "label": "Year 2 — Predict", "shade": "#f8f8f8"},
    {"start": 25, "end": 36, "label": "Year 3 — Synthesis", "shade": "#f5f7fb"},
]

WORKSTREAM_COLORS = {
    "Data and diagnostics": "#36658a",
    "Empirical validation": "#2e7d5b",
    "Comparative modeling": "#7a5195",
    "Reduced model development": "#c06c4e",
    "Infrastructure and reproducibility": "#5f6b7a",
    "Synthesis, release, and adoption": "#9c4f70",
}

GROUP_LABEL_LINES = {
    "Infrastructure and reproducibility": ["Infrastructure and", "reproducibility"],
    "Synthesis, release, and adoption": ["Synthesis, release,", "and adoption"],
}

TASKS = [
    ("Data and diagnostics", "Unified event dataset", 1, 10),
    ("Data and diagnostics", "Extract A(t), P(t)", 2, 12),
    ("Data and diagnostics", "Estimate sigma", 5, 12),
    ("Data and diagnostics", "Detect transitions", 7, 14),
    ("Empirical validation", "Cross-dataset UQ", 8, 20),
    ("Empirical validation", "Resolution sensitivity", 9, 22),
    ("Empirical validation", "Validation and UQ", 10, 36),
    ("Comparative modeling", "Shared event benchmarks", 13, 24),
    ("Comparative modeling", "Diagnostic space evaluation", 14, 26),
    ("Comparative modeling", "Structural and outcome metrics", 15, 27),
    ("Comparative modeling", "Regime-aware performance", 18, 30),
    ("Reduced model development", "Reduced geometry model", 24, 33),
    ("Reduced model development", "Transition-aware gating", 25, 34),
    ("Reduced model development", "Integrate dA/dt = beta(t) * A^(2/3)", 26, 35),
    ("Reduced model development", "Validate A(t), P(t), sigma", 28, 36),
    ("Infrastructure and reproducibility", "Data harmonization", 1, 36),
    ("Infrastructure and reproducibility", "Reproducible code and containers", 1, 36),
    ("Infrastructure and reproducibility", "Benchmark pipelines", 12, 36),
    ("Synthesis, release, and adoption", "Public release", 30, 36),
    ("Synthesis, release, and adoption", "Explorer integration", 31, 36),
    ("Synthesis, release, and adoption", "User evaluation and scenarios", 32, 36),
]

MILESTONES = [
    ("Unified dataset complete", 10, "Data and diagnostics"),
    ("Transition detection validated", 14, "Empirical validation"),
    ("Cross-dataset UQ complete", 20, "Empirical validation"),
    ("Comparative benchmark complete", 24, "Comparative modeling"),
    ("Model discrimination gate", 27, "Comparative modeling"),
    ("Reduced model operational", 33, "Reduced model development"),
    ("Public release complete", 35, "Synthesis, release, and adoption"),
    ("Explorer integration complete", 36, "Synthesis, release, and adoption"),
]


def build_rows() -> tuple[list[dict[str, object]], dict[str, float]]:
    rows: list[dict[str, object]] = []
    group_centers: dict[str, float] = {}
    y = 0.0

    for group in WORKSTREAM_COLORS:
        group_tasks = [t for t in TASKS if t[0] == group]
        start_y = y
        for _, label, start, end in group_tasks:
            rows.append({"group": group, "label": label, "start": start, "duration": end - start + 1, "y": y})
            y += ROW_STEP
        group_centers[group] = (start_y + y - ROW_STEP) / 2
        y += GROUP_GAP

    return rows, group_centers


def render_svg_fallback() -> None:
    rows, group_centers = build_rows()
    width, height = 3300, 2200
    left_label_x = 60
    task_label_x = 790
    chart_x0 = 1340
    chart_x1 = 2660
    milestone_text_x = 2800
    chart_w = chart_x1 - chart_x0
    top = 240
    row_h = 58
    bar_h = 30
    max_y = max(float(r["y"]) for r in rows) + 0.8

    def month_x(month: float) -> float:
        return chart_x0 + ((month - 0.5) / TOTAL_MONTHS) * chart_w

    def row_y(y: float) -> float:
        return top + y * row_h

    parts: list[str] = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    parts.append('<rect width="100%" height="100%" fill="#ffffff"/>')

    # Title
    parts.append('<text x="70" y="80" font-size="56" font-family="Arial, Helvetica, sans-serif" font-weight="700" fill="#111827">FIRE-MODEL Work Plan Gantt Chart</text>')
    parts.append('<text x="70" y="126" font-size="30" font-family="Arial, Helvetica, sans-serif" fill="#475569">Three-track pipeline for Verify, Predict, and Synthesis</text>')

    # Year bands
    for phase in PHASES:
        x0 = month_x(phase["start"])
        x1 = month_x(phase["end"] + 1)
        parts.append(f'<rect x="{x0:.1f}" y="{top-20}" width="{x1-x0:.1f}" height="{(max_y+0.8)*row_h:.1f}" fill="{phase["shade"]}"/>')
        parts.append(f'<text x="{(x0+x1)/2:.1f}" y="{top-52}" text-anchor="middle" font-size="34" font-weight="700" font-family="Arial, Helvetica, sans-serif" fill="#1f2933">{escape(phase["label"])}</text>')

    # Grid lines
    for m in range(1, TOTAL_MONTHS + 1):
        x = month_x(m)
        thick = ((m - 1) % 3 == 0)
        color = "#c7ced6" if thick else "#e5e9ee"
        stroke_w = 2 if thick else 1
        parts.append(f'<line x1="{x:.1f}" y1="{top-20}" x2="{x:.1f}" y2="{row_y(max_y)+row_h:.1f}" stroke="{color}" stroke-width="{stroke_w}"/>')
    for y_end in (12, 24, 36):
        x = month_x(y_end + 1)
        parts.append(f'<line x1="{x:.1f}" y1="{top-28}" x2="{x:.1f}" y2="{row_y(max_y)+row_h:.1f}" stroke="#9aa5b1" stroke-width="3"/>')

    # Tasks and labels
    for row in rows:
        y = row_y(float(row["y"]))
        start = float(row["start"])
        dur = float(row["duration"])
        x = month_x(start)
        w = (dur / TOTAL_MONTHS) * chart_w
        color = WORKSTREAM_COLORS[str(row["group"])]
        parts.append(f'<rect x="{x+2:.1f}" y="{y+((row_h-bar_h)/2):.1f}" width="{max(2,w-4):.1f}" height="{bar_h}" rx="8" fill="{color}" stroke="#ffffff" stroke-width="1"/>')
        parts.append(f'<text x="{task_label_x}" y="{y+37:.1f}" font-size="28" font-family="Arial, Helvetica, sans-serif" fill="#243b53">{escape(str(row["label"]))}</text>')

    # Group labels (wrapped for long labels to preserve large font and avoid overlap)
    for group, y0 in group_centers.items():
        lines = GROUP_LABEL_LINES.get(group, [group])
        if len(lines) == 1:
            parts.append(f'<text x="{left_label_x}" y="{row_y(y0)+37:.1f}" font-size="28" font-family="Arial, Helvetica, sans-serif" font-weight="700" fill="#1f2933">{escape(group)}</text>')
            continue

        line_gap = 26
        text_top_y = row_y(y0) + 24 - ((len(lines) - 1) * line_gap) / 2
        parts.append(
            f'<text x="{left_label_x}" y="{text_top_y:.1f}" font-size="28" font-family="Arial, Helvetica, sans-serif" font-weight="700" fill="#1f2933">'
        )
        for idx, line in enumerate(lines):
            dy = 0 if idx == 0 else line_gap
            parts.append(f'<tspan x="{left_label_x}" dy="{dy}">{escape(line)}</tspan>')
        parts.append("</text>")

    # Milestones with right-column labels and leader lines (staggered)
    for idx, (label, month, group) in enumerate(MILESTONES):
        x = month_x(month)
        y = row_y(group_centers[group]) + row_h / 2
        y_text = top + 24 + idx * 60
        d = 10
        pts = f"{x:.1f},{y-d:.1f} {x+d:.1f},{y:.1f} {x:.1f},{y+d:.1f} {x-d:.1f},{y:.1f}"
        parts.append(f'<polygon points="{pts}" fill="#111827" stroke="#ffffff" stroke-width="1.5"/>')
        parts.append(f'<line x1="{x+12:.1f}" y1="{y:.1f}" x2="{milestone_text_x-14:.1f}" y2="{y_text-6:.1f}" stroke="#64748b" stroke-width="1.4"/>')
        parts.append(f'<text x="{milestone_text_x:.1f}" y="{y_text:.1f}" font-size="22" font-family="Arial, Helvetica, sans-serif" fill="#334155">{escape(label)}</text>')

    # X-axis labels (quarterly)
    for m in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
        parts.append(f'<text x="{month_x(m):.1f}" y="{row_y(max_y)+row_h+46:.1f}" text-anchor="middle" font-size="21" font-family="Arial, Helvetica, sans-serif" fill="#334155">M{m}</text>')
    parts.append(f'<text x="{(chart_x0+chart_x1)/2:.1f}" y="{row_y(max_y)+row_h+92:.1f}" text-anchor="middle" font-size="24" font-family="Arial, Helvetica, sans-serif" font-weight="700" fill="#334155">Project month (quarterly ticks)</text>')

    # Compact legend
    lx, ly = 70, row_y(max_y) + row_h + 130
    for idx, (group, color) in enumerate(WORKSTREAM_COLORS.items()):
        col = idx % 2
        row = idx // 2
        x = lx + col * 540
        y = ly + row * 34
        parts.append(f'<rect x="{x}" y="{y-16}" width="18" height="18" fill="{color}"/>')
        parts.append(f'<text x="{x+28}" y="{y-1}" font-size="17" font-family="Arial, Helvetica, sans-serif" fill="#1f2933">{escape(group)}</text>')

    parts.append('</svg>')
    SVG_PATH.write_text("\n".join(parts), encoding="utf-8")


def render_chart_matplotlib(write_png: bool, write_pdf: bool) -> None:
    rows, group_centers = build_rows()
    fig, ax = plt.subplots(figsize=(21.0, 16.5))
    max_y = max(row["y"] for row in rows) + 0.8

    for phase in PHASES:
        ax.axvspan(phase["start"] - 0.5, phase["end"] + 0.5, color=phase["shade"], zorder=0)
        center = (phase["start"] + phase["end"]) / 2
        ax.text(center, -2.0, phase["label"], ha="center", va="bottom", fontsize=19, fontweight="bold", color="#1f2933")

    for m in range(1, TOTAL_MONTHS + 1):
        lw = 1.2 if (m - 1) % 3 == 0 else 0.5
        color = "#c7ced6" if (m - 1) % 3 == 0 else "#e5e9ee"
        ax.vlines(m - 0.5, -0.5, max_y, color=color, linewidth=lw, zorder=1)

    for year_end in (12, 24, 36):
        ax.vlines(year_end + 0.5, -1.7, max_y, color="#9aa5b1", linewidth=2.2, zorder=2)

    for row in rows:
        y = float(row["y"])
        group = str(row["group"])
        ax.barh(y, float(row["duration"]), left=float(row["start"]) - 0.5, height=0.78, color=WORKSTREAM_COLORS[group], edgecolor="white", linewidth=1.0, zorder=3)
        ax.text(-14.7, y, str(row["label"]), ha="left", va="center", fontsize=15.2, color="#243b53")

    for group, center_y in group_centers.items():
        wrapped = "\n".join(GROUP_LABEL_LINES.get(group, [group]))
        ax.text(
            -30.6,
            center_y,
            wrapped,
            ha="left",
            va="center",
            fontsize=15.6,
            fontweight="bold",
            color="#1f2933",
            linespacing=1.0,
        )

    milestone_text_x = 40.2
    for idx, (label, month, group) in enumerate(MILESTONES):
        y = group_centers[group]
        ax.scatter([month], [y], marker="D", s=80, color="#111827", edgecolors="white", linewidths=0.9, zorder=6)
        label_y = -0.3 + idx * 0.78
        ax.plot([month + 0.15, milestone_text_x - 0.22], [y, label_y], color="#64748b", linewidth=1.0, zorder=5)
        ax.text(milestone_text_x, label_y, label, fontsize=11.8, color="#334155", va="center", ha="left")

    ax.set_xlim(-33.2, 44.9)
    ax.set_ylim(-2.5, max_y + 0.6)
    ax.invert_yaxis()
    ax.set_yticks([])
    quarter_ticks = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    ax.set_xticks(quarter_ticks)
    ax.set_xticklabels([f"M{m}" for m in quarter_ticks], fontsize=13)
    ax.set_xlabel("Project month (quarterly ticks)", fontsize=15, fontweight="bold")
    ax.set_title("FIRE-MODEL Work Plan Gantt Chart", loc="left", fontsize=30, fontweight="bold", pad=26)
    ax.text(-32.8, -2.95, "Three-track pipeline for Verify, Predict, and Synthesis", fontsize=16, color="#475569", va="top")

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="x", length=0, colors="#334155")

    handles = [Line2D([0], [0], marker="s", color="w", markerfacecolor=color, markersize=8, label=group) for group, color in WORKSTREAM_COLORS.items()]
    handles.append(Line2D([0], [0], marker="D", color="w", markerfacecolor="#111827", markeredgecolor="white", markersize=8, label="Milestone"))
    ax.legend(handles=handles, frameon=False, ncol=2, fontsize=10.5, loc="lower left", bbox_to_anchor=(0.0, -0.22), columnspacing=1.1, handletextpad=0.45)

    plt.tight_layout()
    fig.savefig(SVG_PATH, bbox_inches="tight")
    if write_png:
        fig.savefig(PNG_PATH, dpi=450, bbox_inches="tight")
    if write_pdf:
        fig.savefig(PDF_PATH, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate FIRE-MODEL Gantt chart assets.")
    parser.add_argument("--all-formats", action="store_true", help="Also write high-DPI PNG and PDF in addition to SVG.")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if plt is None:
        render_svg_fallback()
        print(f"Saved {SVG_PATH} (pure-Python SVG fallback)")
        if args.all_formats:
            print("Skipped PNG/PDF: matplotlib is not installed")
        return

    render_chart_matplotlib(write_png=args.all_formats, write_pdf=args.all_formats)
    print(f"Saved {SVG_PATH}")
    if args.all_formats:
        print(f"Saved {PNG_PATH}")
        print(f"Saved {PDF_PATH}")
    else:
        print("Skipped PNG/PDF (use --all-formats to generate print assets)")


if __name__ == "__main__":
    main()
