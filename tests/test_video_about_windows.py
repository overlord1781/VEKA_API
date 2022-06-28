from helpers.methods.videos.video_about_windows import Video_about_windows
from helpers.data_test import end_point


def test_video_reviews_200():
    result = Video_about_windows.status_code(end_point['video_reviews'])
    assert result.status_code == 200


def test_helpful_video_200():
    result = Video_about_windows.status_code(end_point['helpful_video'])
    assert result.status_code == 200


def test_helpful_video_partners_200():
    result = Video_about_windows.status_code(end_point['helpful_video_partners'])
    assert result.status_code == 200
