from helpers.methods.videos.video_about_windows import Video_about_windows
from helpers.data_test import end_point

import allure
import time
import datetime
now = datetime.datetime.now()
title = "Получение страницы Видео об окнах с параметром"

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 - {title} video_reviews {now.strftime("%d-%m-%Y %H:%M")} ')
def test_video_reviews_200():
    vaw = Video_about_windows(end_point['video_reviews'])
    assert vaw.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 - {title} helpful_video" {now.strftime("%d-%m-%Y %H:%M")} ')
def test_helpful_video_200():
    vaw = Video_about_windows(end_point['helpful_video'])
    assert vaw.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка статус кода 200')
@allure.title(f'Проверка статус кода 200 - {title} helpful_video_partners" {now.strftime("%d-%m-%Y %H:%M")} ')
def test_helpful_video_partners_200():
    vaw = Video_about_windows(end_point['helpful_video_partners'])
    assert vaw.get_status_code() == 200

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} video_reviews {now.strftime("%d-%m-%Y %H:%M")}')
def test_data_video_reviews():
    vaw = Video_about_windows(end_point['video_reviews'])
    assert vaw.get_data()

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} helpful_video {now.strftime("%d-%m-%Y %H:%M")}')
def test_data_helpful_video():
    vaw = Video_about_windows(end_point['helpful_video'])
    assert vaw.get_data()

@allure.epic('VEKA')
@allure.feature('Проверка получаемого JSON')
@allure.title(f'Проверка получаемого JSON {title} helpful_video_partners {now.strftime("%d-%m-%Y %H:%M")}')
def test_data_helpful_video_partners():
    vaw = Video_about_windows(end_point['helpful_video_partners'])
    assert vaw.get_data()
