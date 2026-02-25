from src.calculators.currency_conversion import calculate_eur, calculate_usd
import pytest

def test_standard_dollar_conversion():
    assert calculate_usd(100, 0.05) == 5.0
    
def test_euro_realistic_conversion():
    assert calculate_eur(250.50, 0.000234) == pytest.approx(0.058617, rel=1e-3)
    
def test_without_money():
    assert calculate_eur(0, 1.25) == 0.0
    assert calculate_usd(0, 1.25) == 0.0
    
def test_zero_currency_rate():
    assert calculate_eur(500, 0) == 0.0
    assert calculate_usd(500, 0) == 0.0