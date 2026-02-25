from src.calculators.body_mass_index_calculator import calculate_imc
import pytest

def test_imc_standard():
    assert calculate_imc(70, 1.75) == pytest.approx(22.857, rel=1e-3)
    
def test_imc_athlete():
    assert calculate_imc(90, 1.90) == pytest.approx(24.93, rel=1e-3)
    
def test_zero_height_bm():
    with pytest.raises(ValueError, match="The height cannot be zero"):
        calculate_imc(70, 0)
        
def test_small_values():
    assert calculate_imc(3.5, 0.5) == 14.0