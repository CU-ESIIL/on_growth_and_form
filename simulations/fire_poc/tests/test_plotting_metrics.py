from __future__ import annotations

import numpy as np

from fire_poc.plotting import _burned_area_and_perimeter


def test_burned_area_and_perimeter_for_two_by_two_block() -> None:
    burned = np.array(
        [
            [False, False, False, False],
            [False, True, True, False],
            [False, True, True, False],
            [False, False, False, False],
        ],
        dtype=bool,
    )
    area_m2, perimeter_m = _burned_area_and_perimeter(burned, cell_size_m=30.0)
    assert area_m2 == 4 * 30.0 * 30.0
    assert perimeter_m == 8 * 30.0
