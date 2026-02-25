from src.calculators.temperature_conversion import celsius_to_fahrenheit, celsius_to_kelvin

def test_positive_temperature():
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_kelvin(100) == 373.15
    
def test_zero_temperature():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_kelvin(0) == 273.15
    
def test_negative_temperatures():
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_kelvin(-273.15) == 0