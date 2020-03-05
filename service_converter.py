from flask import Flask
from converter import Converter

def isnumeric(value):
    try:
        float(value)
        return True
    except Exception:
        return False

converter = Converter()

def yard_to_meter(yard):
    assert isnumeric(yard), '%s should be numeric' % yard
    return converter.yard_to_meter(float(yard))

def meter_to_yard(meter):
    converter = Converter()
    return str(converter.meter_to_yard(float(meter)))