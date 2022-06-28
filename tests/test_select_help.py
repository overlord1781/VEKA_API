from helpers.methods.pages.select_help import Select_help
from helpers.data_test import end_point


def test_200():
    result = Select_help.status_code(end_point['select_help'])
    assert result.status_code == 200

