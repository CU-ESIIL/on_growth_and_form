"""Simple geometry helpers for perimeter generation and area calculation."""

from __future__ import annotations

import math

import numpy as np


def ellipse_perimeter(
    center_xy: tuple[float, float],
    semi_major_m: float,
    semi_minor_m: float,
    angle_deg: float,
    n_points: int = 240,
) -> np.ndarray:
    """Return a rotated ellipse perimeter."""

    theta = np.linspace(0.0, 2.0 * math.pi, n_points, endpoint=False)
    x = semi_major_m * np.cos(theta)
    y = semi_minor_m * np.sin(theta)
    angle_rad = math.radians(angle_deg)
    rotation = np.array(
        [
            [math.cos(angle_rad), -math.sin(angle_rad)],
            [math.sin(angle_rad), math.cos(angle_rad)],
        ]
    )
    pts = np.column_stack((x, y)) @ rotation.T
    pts[:, 0] += center_xy[0]
    pts[:, 1] += center_xy[1]
    return pts


def polygon_area(coords: np.ndarray) -> float:
    """Compute polygon area via the shoelace formula."""

    x = coords[:, 0]
    y = coords[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


def area_series(perimeters: list[np.ndarray]) -> np.ndarray:
    """Compute area for a sequence of perimeters."""

    return np.asarray([polygon_area(perimeter) for perimeter in perimeters], dtype=float)

