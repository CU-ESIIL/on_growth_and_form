from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path("/tmp") / "matplotlib-on-growth-and-form"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = REPO_ROOT / "docs" / "assets" / "figures" / "wildfire_phylogeny_publication.png"


# The trunk marks broad historical transitions in wildfire modeling.
# Years are used directly on the x-axis so the figure reads as a time-calibrated
# conceptual phylogeny rather than a categorical flowchart.
TRUNK_NODES = [
    (1930, "Early observation\nand fire-danger systems", 1.62, 1930.0),
    (1972, "Rothermel", 1.62, 1972.0),
    (1998, "Spatial growth turn", 1.85, 1999.0),
    (2005, "Probabilistic /\nrisk turn", 1.38, 2006.0),
    (2020, "Data-rich /\nML era", 1.62, 2020.0),
]

TRUNK_SEGMENTS = [
    (1930, 1972, "Computable local spread", 0.74),
    (1972, 1998, "Wavefront perimeter growth", 0.74),
    (1998, 2005, "Ensemble risk simulation", 0.70),
    (2005, 2020, "ML and data-driven prediction", 0.56),
]

# Branches encode conceptual descent or use-case divergence from the trunk.
# Each branch starts from an anchor year on the trunk, rises or falls into its
# own lane, and terminates at a tip model placed at the historically relevant year.
BRANCHES = [
    {
        "anchor": 1972,
        "tip_year": 1976,
        "tip_label": "Albini (1976)",
        "innovation": "Behavior extensions",
        "y": 2.6,
        "color": "#bc5a45",
    },
    {
        "anchor": 1972,
        "tip_year": 1982,
        "tip_label": "Anderson (1982)",
        "innovation": "Fuel standardization",
        "y": 4.1,
        "color": "#c97a40",
    },
    {
        "anchor": 1982,
        "tip_year": 1996,
        "tip_label": "Canadian FBP (1996)",
        "innovation": "Operational systems",
        "y": 5.6,
        "color": "#d4973f",
    },
    {
        "anchor": 1972,
        "tip_year": 1998,
        "tip_label": "FARSITE (1998)",
        "innovation": "Wavefront simulation",
        "y": 1.25,
        "color": "#7d8f44",
        "tip_dx": 0.7,
        "tip_dy": 0.28,
        "innovation_y_offset": 0.34,
    },
    {
        "anchor": 1998,
        "tip_year": 2002,
        "tip_label": "MTT (2002)",
        "innovation": "Minimum travel time",
        "y": 2.0,
        "color": "#5f8b59",
        "tip_dx": 0.72,
        "tip_dy": 0.54,
        "innovation_y_offset": 0.42,
    },
    {
        "anchor": 2005,
        "tip_year": 2011,
        "tip_label": "FSim (2011)",
        "innovation": "Probabilistic risk",
        "y": 0.95,
        "color": "#397e72",
        "tip_dx": 0.72,
        "tip_dy": -0.2,
        "innovation_y_offset": 0.14,
    },
    {
        "anchor": 1930,
        "tip_year": 1996,
        "tip_label": "Clark et al. (1996)",
        "innovation": "Coupled fire-atmosphere",
        "y": -2.45,
        "color": "#39708d",
        "tip_dx": 0.6,
        "tip_dy": -0.18,
        "innovation_y_offset": -0.36,
    },
    {
        "anchor": 1996,
        "tip_year": 2013,
        "tip_label": "WRF-Fire (2013)",
        "innovation": "Weather-fire coupling",
        "y": -3.7,
        "color": "#2f5f81",
        "innovation_y_offset": -0.30,
    },
    {
        "anchor": 1930,
        "tip_year": 1997,
        "tip_label": "Cellular automata (1997)",
        "innovation": "Local-rule emergence",
        "y": -0.95,
        "color": "#8f5e7e",
        "tip_dx": 0.58,
        "tip_dy": 0.18,
        "innovation_y_offset": -0.26,
    },
    {
        "anchor": 1997,
        "tip_year": 1998,
        "tip_label": "Malamud et al. (1998)",
        "innovation": "Scaling / criticality",
        "y": -1.7,
        "color": "#7f4b77",
        "tip_dx": 0.62,
        "tip_dy": -0.18,
        "innovation_y_offset": -0.26,
    },
    {
        "anchor": 1930,
        "tip_year": 2004,
        "tip_label": "LANDIS (2004)",
        "innovation": "Landscape ecology",
        "y": -5.05,
        "color": "#55734d",
        "tip_dx": 0.62,
        "tip_dy": -0.18,
        "innovation_y_offset": -0.30,
    },
    {
        "anchor": 2004,
        "tip_year": 2007,
        "tip_label": "LANDIS-II (2007)",
        "innovation": "Modular ecosystem",
        "y": -6.3,
        "color": "#3f6241",
        "innovation_y_offset": -0.32,
    },
    {
        "anchor": 2005,
        "tip_year": 2020,
        "tip_label": "ML wildfire models (2020)",
        "innovation": "ML prediction",
        "y": -7.6,
        "color": "#8f6c2c",
        "innovation_y_offset": -0.28,
    },
]


def draw_branch(ax: plt.Axes, branch: dict[str, object]) -> None:
    anchor = float(branch["anchor"])
    tip_year = float(branch["tip_year"])
    y = float(branch["y"])
    color = str(branch["color"])
    innovation = str(branch["innovation"])
    tip_label = str(branch["tip_label"])

    elbow_year = anchor + max((tip_year - anchor) * 0.22, 2.0)
    if tip_year - anchor < 4:
        elbow_year = anchor + (tip_year - anchor) * 0.45

    xs = [anchor, elbow_year, tip_year]
    ys = [0.0, y, y]
    ax.plot(
        xs,
        ys,
        color=color,
        linewidth=4.8,
        solid_capstyle="round",
        solid_joinstyle="round",
        zorder=3,
    )

    ax.scatter([tip_year], [y], s=90, color=color, edgecolor="white", linewidth=1.2, zorder=4)

    label_dx = float(branch.get("tip_dx", 0.65))
    label_dy = float(branch.get("tip_dy", 0.22 if y >= 0 else -0.22))
    ax.text(
        tip_year + label_dx,
        y + label_dy,
        tip_label,
        fontsize=13.5,
        color="#17211d",
        va="center",
        ha="left",
        zorder=5,
    )

    mid_x = (anchor + tip_year) / 2
    innovation_y = y + float(branch.get("innovation_y_offset", 0.38 if y >= 0 else -0.38))
    va = "bottom" if y >= 0 else "top"
    ax.text(
        mid_x,
        innovation_y,
        innovation,
        fontsize=12,
        color=color,
        fontweight="bold",
        ha="center",
        va=va,
        bbox={"boxstyle": "round,pad=0.22", "fc": "white", "ec": "none", "alpha": 0.9},
        zorder=6,
    )


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.edgecolor": "#45514a",
            "axes.linewidth": 1.2,
            "xtick.color": "#45514a",
            "ytick.color": "#45514a",
        }
    )

    fig, ax = plt.subplots(figsize=(19, 10.5), dpi=220)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    start_year = 1928
    end_year = 2023
    ax.set_xlim(start_year, end_year)
    ax.set_ylim(-8.8, 7.0)

    ax.axhline(0, color="#d8ddd8", linewidth=1.1, zorder=0)

    for x0, x1, label, label_y in TRUNK_SEGMENTS:
        ax.plot([x0, x1], [0, 0], color="#23352d", linewidth=8.2, solid_capstyle="round", zorder=2)
        ax.text(
            (x0 + x1) / 2,
            label_y,
            label,
            fontsize=12.8,
            fontweight="bold",
            color="#23352d",
            ha="center",
            va="bottom",
            bbox={"boxstyle": "round,pad=0.22", "fc": "#f6f7f4", "ec": "none", "alpha": 0.98},
            zorder=7,
        )

    for year, label, label_y, label_x in TRUNK_NODES:
        ax.scatter([year], [0], s=145, color="#23352d", edgecolor="white", linewidth=1.5, zorder=4)
        ax.text(
            label_x,
            label_y,
            f"{label}\n({year})" if year != 1972 else "Rothermel\n(1972)",
            fontsize=13.2,
            ha="center",
            va="bottom",
            color="#17211d",
            zorder=8,
        )

    for branch in BRANCHES:
        draw_branch(ax, branch)

    ax.set_xlabel("Calendar year", fontsize=15, labelpad=14, color="#17211d")
    ax.set_yticks([])
    ax.set_xticks([1930, 1940, 1950, 1960, 1972, 1980, 1990, 1998, 2005, 2013, 2020])
    ax.tick_params(axis="x", labelsize=12.5, length=6, width=1.2)

    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    ax.grid(axis="x", color="#eef1ec", linewidth=0.9)

    fig.suptitle(
        "Conceptual time-calibrated phylogeny of wildfire modeling",
        fontsize=22,
        fontweight="bold",
        x=0.5,
        y=0.975,
        color="#17211d",
    )
    ax.set_title(
        "Historical trunk transitions, conceptual branch innovations, and representative model tips",
        fontsize=14.5,
        pad=18,
        color="#45514a",
    )

    fig.text(
        0.012,
        0.022,
        "Conceptual figure: branch structure encodes intellectual descent and use-case divergence, not strict software inheritance.",
        fontsize=11.5,
        color="#5a665f",
    )

    fig.subplots_adjust(left=0.055, right=0.985, top=0.89, bottom=0.12)
    fig.savefig(OUTPUT_PATH, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
