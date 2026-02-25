from src.calculators.calculator_energy_consumption_of_a_computer import energy_consumption
import pytest

def test_standard_computer():
    assert energy_consumption(100, 8) == 24.0
    
def test_powerful_gaming_computer():
    assert energy_consumption(500, 4.5) == pytest.approx(67.5, rel=1e-3)
    
def test_computer_off():
    assert energy_consumption(200, 0) == 0.0
    
def test_minimum_power():
    assert energy_consumption(5, 24) == 3.6