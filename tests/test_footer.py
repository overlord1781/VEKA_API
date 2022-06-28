from helpers.methods.common.footer import Footer
from helpers.data_test import end_point


def test_200():
    result = Footer.status_code(end_point['footer'])
    assert result.status_code == 200

