from helpers.methods.common.detect_city import Detect_city
from helpers.data_test import end_point

import allure
import time
import datetime
now = datetime.datetime.now()
title = "Запрос на определение города"

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 {title} {now.strftime("%d-%m-%Y %H:%M")} ')
def test_200():
    detect_city = Detect_city(end_point['detect_city'])
    assert detect_city.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} {now.strftime("%d-%m-%Y %H:%M")}')
def test_data():
    detect_city = Detect_city(end_point['detect_city'])
    assert detect_city.get_data()