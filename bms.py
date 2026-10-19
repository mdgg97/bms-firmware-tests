MAX_CELL_VOLTAGE = 4.20
MIN_CELL_VOLTAGE = 2.70
MAX_CELL_TEMPERATURE = 60.0

def is_voltage_safe(voltage):
    return MIN_CELL_VOLTAGE <= voltage <= MAX_CELL_VOLTAGE