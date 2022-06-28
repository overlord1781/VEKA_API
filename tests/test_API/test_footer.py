from helpers.methods.common.footer import Footer
from helpers.data_test import end_point

import allure
import time
import datetime
now = datetime.datetime.now()
title = "Запрос на получение данных для футера"

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 {title} {now.strftime("%d-%m-%Y %H:%M")} ')
def test_200():
    footer = Footer(end_point['footer'])
    assert footer.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} {now.strftime("%d-%m-%Y %H:%M")}')
def test_data():
    footer = Footer(end_point['footer'])
    assert footer.get_data()