from helpers.methods.common.cities import Cities
from helpers.data_test import end_point


def test_200():
    result = Cities.status_code(end_point['cities'])
    assert result.status_code == 200

