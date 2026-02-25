from src.calculators.euclidean_distance_calculator import euclidean_distance
import pytest

def test_exact_pythagorean_distance():
    assert euclidean_distance(0, 0, 3, 4) == 5.0
    
def test_points_same_place():
    assert euclidean_distance(10, 10, 10, 10) == 0.0
    
def test_distance_with_decimals():
    assert euclidean_distance(1.5, 2.5, 4.1, 9.8) == pytest.approx(7.749, rel=1e-3)
    
def test_negative_distance():
    assert euclidean_distance(-1, -1, -4, -5) == 5.0