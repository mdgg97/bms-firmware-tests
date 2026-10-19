
import  pytest 

from bms import is_voltage_safe

@pytest.mark.parametrize("voltage,expected", [ 




    (2.69, False),
    (2.70, True),
    (3.70, True),
    (4.20, True),
    (4.21, False),



])

def test_voltage_safety(voltage,expected):
    assert is_voltage_safe(voltage) == expected
    
