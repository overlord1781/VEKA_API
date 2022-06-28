from helpers.methods.videos.videos import Videos
from helpers.data_test import end_point


def test_video_reviews_200():
    result = Videos.status_code(end_point['videos_video_reviews'])
    assert result.status_code == 200


def test_helpful_video_200():
    result = Videos.status_code(end_point['videos_helpful_video'])
    assert result.status_code == 200


def test_helpful_video_partners_200():
    result = Videos.status_code(end_point['videos_helpful_video_partners'])
    assert result.status_code == 200
