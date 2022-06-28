from helpers.methods.videos.videos import Videos
from helpers.data_test import end_point

import allure
import time
import datetime
now = datetime.datetime.now()
title = "Получение видео с параметром"

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 {title} videos_video_reviews {now.strftime("%d-%m-%Y %H:%M")} ')
def test_video_reviews_200():
    videos = Videos(end_point['videos_video_reviews'])
    assert videos.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 {title} videos_helpful_video {now.strftime("%d-%m-%Y %H:%M")} ')
def test_helpful_video_200():
    videos = Videos(end_point['videos_helpful_video'])
    assert videos.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 {title} videos_helpful_video_partners {now.strftime("%d-%m-%Y %H:%M")} ')
def test_helpful_video_partners_200():
    videos = Videos(end_point['videos_helpful_video_partners'])
    assert videos.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} videos_video_reviews {now.strftime("%d-%m-%Y %H:%M")}')
def test_data_video_reviews():
    videos = Videos(end_point['videos_video_reviews'])
    assert videos.get_data()

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} videos_helpful_video {now.strftime("%d-%m-%Y %H:%M")}')
def test_data_helpful_video():
    videos = Videos(end_point['videos_helpful_video'])
    assert videos.get_data()

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} videos_helpful_video_partners {now.strftime("%d-%m-%Y %H:%M")}')
def test_data_helpful_video_partners():
    videos = Videos(end_point['videos_helpful_video_partners'])
    assert videos.get_data()


