from helpers.methods.videos.video_reviews import Video_reviews
from helpers.data_test import end_point


def test_200():
    result = Video_reviews.status_code(end_point['video_rws'])
    assert result.status_code == 200
