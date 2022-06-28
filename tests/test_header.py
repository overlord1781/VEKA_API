from helpers.methods.common.header import Header
from helpers.data_test import end_point


def test_200():
    result = Header.status_code(end_point['header'])
    assert result.status_code == 200

