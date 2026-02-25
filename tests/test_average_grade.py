from src.calculators.average_grade import calculate_average
import pytest

def test_perfect_average():
    assert calculate_average(10, 10, 10, 10) == 10.0
    
def test_zero_average():
    assert calculate_average(0, 0, 0, 0) == 0.0
    
def test_average_of_mixed_decimals():
    assert calculate_average(7.5, 8.2, 9.0, 6.4) == pytest.approx(7.775, rel=1e-3)
    
def test_average_a_high_grade():
    assert calculate_average(10, 2, 2, 2) == 4.0