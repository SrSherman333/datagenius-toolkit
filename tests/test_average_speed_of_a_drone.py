from src.calculators.average_speed_of_a_drone import speed_kmh, speed_ms
import pytest

def test_exact_speed():
    v_kmh = speed_kmh(100, 2)
    assert v_kmh == 50.0
    assert speed_ms(v_kmh) == pytest.approx(13.888, rel=1e-3)
    
def test_famous_conversion():
    assert speed_ms(36) == 10.0
    
def test_static_drone():
    assert speed_kmh(0, 5) == 0.0
    assert speed_ms(0) == 0.0
    
def test_zero_time_drone():
    with pytest.raises(ValueError, match="Time cannot be zero"):
        speed_kmh(10, 0)