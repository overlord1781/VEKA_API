from helpers.methods.select_help.select_help_result import Select_help_result
from helpers.data_test import end_point


def test_200():
    result = Select_help_result.status_code(end_point['select_help_result'])
    assert result.status_code == 200

