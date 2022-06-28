from helpers.methods.common.detect_city import Detect_city
from helpers.data_test import end_point


def test_200():
    result = Detect_city.status_code(end_point['detect_city'])
    assert result.status_code == 200