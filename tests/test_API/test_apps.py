from helpers.methods.pages.apps import Apps
from helpers.data_test import end_point

import allure
import time
import datetime
now = datetime.datetime.now()
title = "Получение страницы Наши приложения"

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 {title} {now.strftime("%d-%m-%Y %H:%M")} ')
def test_200():
    apps = Apps(end_point['apps'])
    assert apps.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} {now.strftime("%d-%m-%Y %H:%M")}')
def test_data():
    apps = Apps(end_point['apps'])
    assert apps.get_data()