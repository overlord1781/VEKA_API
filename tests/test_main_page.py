from helpers.methods.pages.apps import Apps
from helpers.data_test import end_point


def test_200():
    result = Apps.status_code(end_point['main_page'])
    assert result.status_code == 200
