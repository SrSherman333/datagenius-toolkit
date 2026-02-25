from src.calculators.execution_time_calculator import time_minutes, time_seconds
import pytest

def test_fast_execution():
    seconds = time_seconds(1000, 100)
    assert seconds == 10
    assert time_minutes(seconds) == pytest.approx(0.166666, rel=1e-3)
    
def test_large_values():
    seconds = time_seconds(1000000, 500)
    assert seconds == 2000
    assert time_minutes(seconds) == pytest.approx(33.3333, rel=1e-3)
    
def test_division_by_zero():
    with pytest.raises(ValueError, match="Velocity cannot be zero"):
        time_seconds(100, 0)