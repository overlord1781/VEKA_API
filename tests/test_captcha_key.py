from helpers.methods.form.captcha_key import Captcha_key
from helpers.data_test import end_point


def test_200():
    result = Captcha_key.status_code(end_point['captcha_key'])
    assert result.status_code == 200

