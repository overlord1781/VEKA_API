from helpers.methods.common.cities import Cities
from helpers.data_test import end_point

import allure
import time
import datetime
now = datetime.datetime.now()
title = "Запрос на получение списка городов или поиск города"

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 {title} {now.strftime("%d-%m-%Y %H:%M")} ')
def test_200():
    cities = Cities(end_point['cities'])
    assert cities.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} {now.strftime("%d-%m-%Y %H:%M")}')
def test_data():
    cities = Cities(end_point['cities'])
    assert cities.get_data()