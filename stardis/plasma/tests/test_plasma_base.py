import pytest

from numpy import allclose

import stardis.plasma.base as plasma_base


@pytest.mark.parametrize("H2Density_input_ion_number_density", range(11))
def test_H2Density_division_by_zero(H2Density_input_ion_number_density):
    with pytest.raises(ZeroDivisionError):
        _ = plasma_base.H2Density.calculate(
            H2Density_input_ion_number_density,
            0,
        )
