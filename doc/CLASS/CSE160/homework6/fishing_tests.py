import math
from fishing import get_production_need

def test_get_production_need():
    # Test case 1: Population and consumption are both available
    data = {
        "population": {"AMP": {1960: 1000000}},
        "consumption": {"AMP": {1960: 10}},
    }
    actual_float = get_production_need(data, "AMP", 1960)
    expected_float = 1000000 * 10 / 1000  
    assert math.isclose(actual_float, expected_float)

    # Test case 2: Population or consumption is missing
    data = {
        "population": {"AMP": {1960: 1000000}},
        "consumption": {"AMP": {1960: None}},
    }
    actual_float = get_production_need(data, "AMP", 1960)
    assert actual_float is None

test_get_production_need()
