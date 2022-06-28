from helpers.methods.videos.video_reviews import Video_reviews
from helpers.data_test import end_point

import allure
import time
import datetime
now = datetime.datetime.now()
title = "Получение страницы видео-отзывов"

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 {title} {now.strftime("%d-%m-%Y %H:%M")} ')
def test_200():
    video_reviews = Video_reviews(end_point['video_rws'])
    assert video_reviews.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} {now.strftime("%d-%m-%Y %H:%M")}')
def test_data():
    video_reviews = Video_reviews(end_point['video_rws'])
    assert video_reviews.get_data()
