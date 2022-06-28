from helpers.methods.select_help.select_help_result import Select_help_result
from helpers.data_test import end_point

import allure
import time
import datetime
now = datetime.datetime.now()
title = "Результат выбора окна"

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 {title} {now.strftime("%d-%m-%Y %H:%M")} ')
def test_200():
    select_help_result = Select_help_result(end_point['select_help_result'])
    assert select_help_result.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} {now.strftime("%d-%m-%Y %H:%M")}')
def test_data():
    select_help_result = Select_help_result(end_point['select_help_result'])
    assert select_help_result.get_data()