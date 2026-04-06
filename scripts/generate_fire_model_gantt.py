from __future__ import annotations

"""Generate the proposal-ready FIRE-MODEL Gantt chart.

Language source: repository proposal timeline language emphasizing
"Year 1 — Verify", "Year 2 — Predict", and "Year 3 — Synthesis",
with overlap across data, validation, modeling, and infrastructure tracks.
"""

from pathlib import Path
import argparse

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "docs" / "assets" / "figures"
BASENAME = "fire_model_gantt_verify_predict_synthesis"
PNG_PATH = OUTPUT_DIR / f"{BASENAME}.png"
PDF_PATH = OUTPUT_DIR / f"{BASENAME}.pdf"
SVG_PATH = OUTPUT_DIR / f"{BASENAME}.svg"

TOTAL_MONTHS = 36

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

# Concise labels are intentional for NSF two-column readability.
TASKS = [
    ("Data and diagnostics", "Unified event dataset (QC)", 1, 10),
    ("Data and diagnostics", "Extract A(t), P(t): FIRED/GOFER/FEDS", 2, 12),
    ("Data and diagnostics", "Estimate σ = d(log P)/d(log A)", 5, 12),
    ("Data and diagnostics", "Detect regime transitions", 7, 14),
    ("Empirical validation", "Cross-dataset uncertainty propagation", 8, 20),
    ("Empirical validation", "Resolution/processing sensitivity", 9, 22),
    ("Empirical validation", "Validation and UQ (continuing)", 10, 36),
    ("Comparative modeling", "Run competing models on shared events", 13, 24),
    ("Comparative modeling", "Shared diagnostic space evaluation", 14, 26),
    ("Comparative modeling", "Structural/dynamical/outcome metrics", 15, 27),
    ("Comparative modeling", "Regime-aware predictive performance tests", 18, 30),
    ("Reduced model development", "Reduced geometry-constrained model", 24, 33),
    ("Reduced model development", "Transition-aware gating", 25, 34),
    ("Reduced model development", "Integrate dA/dt = β(t) · A^(2/3)", 26, 35),
    ("Reduced model development", "Validate A(t), P(t), σ trajectories", 28, 36),
    ("Infrastructure and reproducibility", "Data ingestion and harmonization", 1, 36),
    ("Infrastructure and reproducibility", "Reproducible code + containers", 1, 36),
    ("Infrastructure and reproducibility", "Benchmark pipelines and stability tests", 12, 36),
    ("Synthesis, release, and adoption", "Public release: code, data, workflows", 30, 36),
    ("Synthesis, release, and adoption", "Fire Dynamics Explorer integration", 31, 36),
    ("Synthesis, release, and adoption", "User-facing evaluation + scenarios", 32, 36),
]

MILESTONES = [
    ("Unified event dataset complete", 10, "Data and diagnostics"),
    ("Transition detection pipeline validated", 14, "Empirical validation"),
    ("Cross-dataset uncertainty assessment complete", 20, "Empirical validation"),
    ("Comparative benchmark complete", 24, "Comparative modeling"),
    ("Model discrimination decision gate", 27, "Comparative modeling"),
    ("Reduced generative model operational", 33, "Reduced model development"),
    ("Public release of code and workflows", 35, "Synthesis, release, and adoption"),
    ("Explorer integration complete", 36, "Synthesis, release, and adoption"),
]


def build_rows() -> tuple[list[dict[str, object]], dict[str, float]]:
    rows: list[dict[str, object]] = []
    group_centers: dict[str, float] = {}
    y = 0.0
    group_gap = 0.9

    groups = list(WORKSTREAM_COLORS.keys())
    for group in groups:
        group_tasks = [t for t in TASKS if t[0] == group]
        start_y = y
        for _, label, start, end in group_tasks:
            rows.append(
                {
                    "group": group,
                    "label": label,
                    "start": start,
                    "duration": end - start + 1,
                    "y": y,
                }
            )
            y += 1.0
        end_y = y - 1.0
        group_centers[group] = (start_y + end_y) / 2
        y += group_gap

    return rows, group_centers


def render_chart(write_png: bool = False, write_pdf: bool = False) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows, group_centers = build_rows()

    fig, ax = plt.subplots(figsize=(18, 12.5))
    fig.patch.set_facecolor("white")

    max_y = max(row["y"] for row in rows) + 0.8

    # Subtle year shading and headers.
    for phase in PHASES:
        ax.axvspan(phase["start"] - 0.5, phase["end"] + 0.5, color=phase["shade"], zorder=0)
        center = (phase["start"] + phase["end"]) / 2
        ax.text(
            center,
            -1.45,
            phase["label"],
            ha="center",
            va="bottom",
            fontsize=17,
            fontweight="bold",
            color="#1f2933",
        )

    # Month grid with stronger quarter and year boundaries.
    for m in range(1, TOTAL_MONTHS + 1):
        lw = 1.2 if (m - 1) % 3 == 0 else 0.5
        color = "#c7ced6" if (m - 1) % 3 == 0 else "#e5e9ee"
        ax.vlines(m - 0.5, -0.5, max_y, color=color, linewidth=lw, zorder=1)

    for year_end in (12, 24, 36):
        ax.vlines(year_end + 0.5, -1.7, max_y, color="#9aa5b1", linewidth=2.2, zorder=2)

    # Task bars and labels.
    for row in rows:
        y = float(row["y"])
        group = str(row["group"])
        color = WORKSTREAM_COLORS[group]
        ax.barh(
            y,
            float(row["duration"]),
            left=float(row["start"]) - 0.5,
            height=0.62,
            color=color,
            edgecolor="white",
            linewidth=1.0,
            zorder=3,
        )
        ax.text(
            -10.1,
            y,
            str(row["label"]),
            ha="left",
            va="center",
            fontsize=12.8,
            color="#243b53",
        )

    # Group headers and separators.
    for group, center_y in group_centers.items():
        ax.text(
            -20.2,
            center_y,
            group,
            ha="left",
            va="center",
            fontsize=13.8,
            fontweight="bold",
            color="#1f2933",
        )

    # Milestones as diamonds on the nearest workstream center.
    for label, month, group in MILESTONES:
        y = group_centers[group]
        ax.scatter(
            [month],
            [y],
            marker="D",
            s=80,
            color="#111827",
            edgecolors="white",
            linewidths=0.9,
            zorder=6,
        )
        ax.text(month + 0.35, y - 0.33, label, fontsize=10.5, color="#334155", va="top")

    ax.set_xlim(-21.0, 36.6)
    ax.set_ylim(-2.0, max_y + 0.4)
    ax.invert_yaxis()
    ax.set_yticks([])

    # Reduce x-label clutter: show quarterly ticks only.
    quarter_ticks = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    ax.set_xticks(quarter_ticks)
    ax.set_xticklabels([f"M{m}" for m in quarter_ticks], fontsize=12)
    ax.set_xlabel("Project month (quarterly ticks)", fontsize=14, fontweight="bold")

    title = "FIRE-MODEL Work Plan Gantt Chart"
    subtitle = "Three-track pipeline for Verify, Predict, and Synthesis"
    ax.set_title(title, loc="left", fontsize=26, fontweight="bold", pad=24)
    ax.text(-20.9, -2.28, subtitle, fontsize=14.5, color="#475569", va="top")

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="x", length=0, colors="#334155")

    handles = [
        Line2D([0], [0], marker="s", color="w", markerfacecolor=color, markersize=10, label=group)
        for group, color in WORKSTREAM_COLORS.items()
    ]
    handles.append(
        Line2D([0], [0], marker="D", color="w", markerfacecolor="#111827", markeredgecolor="white", markersize=8, label="Milestone")
    )

    ax.legend(
        handles=handles,
        frameon=False,
        ncol=2,
        fontsize=11.2,
        loc="lower left",
        bbox_to_anchor=(0.0, -0.23),
        columnspacing=1.3,
        handletextpad=0.5,
    )

    plt.tight_layout()
    fig.savefig(SVG_PATH, bbox_inches="tight")
    if write_png:
        fig.savefig(PNG_PATH, dpi=450, bbox_inches="tight")
    if write_pdf:
        fig.savefig(PDF_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate FIRE-MODEL Gantt chart assets.")
    parser.add_argument("--all-formats", action="store_true", help="Also write high-DPI PNG and PDF in addition to SVG.")
    args = parser.parse_args()

    render_chart(write_png=args.all_formats, write_pdf=args.all_formats)
    print(f"Saved {SVG_PATH}")
    if args.all_formats:
        print(f"Saved {PNG_PATH}")
        print(f"Saved {PDF_PATH}")
    else:
        print("Skipped PNG/PDF (use --all-formats to generate print assets)")
