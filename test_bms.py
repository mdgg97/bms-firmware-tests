from bms import is_voltage_safe

def test_normal_voltage_is_safe():
    assert is_voltage_safe(3.70) == True

def test_overvoltage_is_not_safe():
    assert is_voltage_safe(4.21) == False

def test_undervoltage_is_not_safe():
    assert is_voltage_safe(2.69) == False

def test_min_voltage_boundary_is_safe():
    assert is_voltage_safe(2.70) == True
