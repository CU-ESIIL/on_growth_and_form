from __future__ import annotations

import math

from fire_poc.geometry import ellipse_perimeter, polygon_area


def test_polygon_area_matches_ellipse_area_reasonably() -> None:
    perimeter = ellipse_perimeter((0.0, 0.0), semi_major_m=10.0, semi_minor_m=4.0, angle_deg=25.0, n_points=1000)
    area = polygon_area(perimeter)
    expected = math.pi * 10.0 * 4.0
    assert abs(area - expected) / expected < 0.02

