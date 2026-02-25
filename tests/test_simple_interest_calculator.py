from src.calculators.simple_interest_calculator import calculate_total_amount, rate_percentage
import pytest

def test_standard_interest():
    i = rate_percentage(5)
    assert calculate_total_amount(1000, i, 2) == 1100.0
    
def test_precise_decimal_interest():
    i = rate_percentage(3.5)
    assert calculate_total_amount(500.50, i, 1.5) == pytest.approx(526.77625, rel=1e-3)
    
def test_time_zero():
    i = rate_percentage(10)
    assert calculate_total_amount(1000, i, 0) == 1000.0
    
def test_zero_rate():
    i = rate_percentage(0)
    assert calculate_total_amount(1000, i, 5) == 1000.0