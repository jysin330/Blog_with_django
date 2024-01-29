from django.core.exceptions import  ValidationError
import pint
from pint.errors import UndefinedUnitError
valid_unit_measurements =['pounds', 'lbs', 'oz', 'gram']
# pint - Pint is a python package to define, operate and manipulate physical Quantities.

def validate_unit_of_measure(value):
    try:
        ureg = pint.UnitRegistry()
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{e} is not a valid unit of measure")
    except:
        raise ValidationError(f"{value} is invalid. Unknown Error.")
    # if value not in valid_unit_measurements:
    #     raise ValidationError(f"{value} is not a valid unit of measure")
    