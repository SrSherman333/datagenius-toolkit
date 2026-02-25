from src.calculators.cloud_storage_cost import monthly_cost, annual_cost
import pytest

def test_standard_calculus():
    monthly = monthly_cost(100, 0.02)
    assert monthly == 2.0
    assert annual_cost(monthly) == 24.0
    
def test_precise_decimal_values():
    monthly = monthly_cost(50.5, 0.1)
    assert monthly == pytest.approx(5.05)
    assert annual_cost(monthly) == pytest.approx(60.6)
    
def test_zero_cost():
    monthly = monthly_cost(0, 0.05)
    assert monthly == 0
    assert annual_cost(monthly) == 0