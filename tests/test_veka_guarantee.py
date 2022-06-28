from helpers.methods.pages.veka_guarantee import Veka_guarantee
from helpers.data_test import end_point


def test_200():
    result = Veka_guarantee.status_code(end_point['veka_guarantee'])
    assert result.status_code == 200

