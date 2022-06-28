from helpers.methods.pages.veka_guarantee import Veka_guarantee
from helpers.data_test import end_point

import allure
import time
import datetime
now = datetime.datetime.now()
title = "Получение страницы VEKAвая гарантия"

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 {title} {now.strftime("%d-%m-%Y %H:%M")} ')
def test_200():
    veka_guarantee = Veka_guarantee(end_point['veka_guarantee'])
    assert veka_guarantee.get_status_code()

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} {now.strftime("%d-%m-%Y %H:%M")}')
def test_data():
    veka_guarantee = Veka_guarantee(end_point['veka_guarantee'])
    assert veka_guarantee.get_data()

