import os

import pytest

from youtube import Channel, Video, PLVideo

PATH_TO_TEST_CHANNEL_1_JSON = os.path.join('tests', 'test_channel_1.json')
PATH_TO_TEST_CHANNEL_2_JSON = os.path.join('tests', 'test_channel_2.json')
PATH_TO_TEST_VIDEO_JSON = os.path.join('tests', 'test_video.json')
PATH_TO_TEST_VIDEO_IN_PLAYLIST_JSON = os.path.join('tests', 'test_video_in_playlist.json')
PATH_TO_VIDEO_IN_PLAYLIST_JSON = os.path.join('tests', 'video_in_playlist.json')
PATH_TO_VIDEO_NOT_PLAYLIST_JSON = os.path.join('tests', 'video_not_playlist.json')


@pytest.fixture
def channel_1_for_test():
    return Channel(channel_json=PATH_TO_TEST_CHANNEL_1_JSON)


@pytest.fixture
def channel_2_for_test():
    return Channel(channel_json=PATH_TO_TEST_CHANNEL_2_JSON)


@pytest.fixture
def channel():
    return Channel(channel_id='UCMCgOm8GZkHp8zJ6l7_hIuA')


@pytest.fixture
def video_for_test():
    return Video(video_json=PATH_TO_TEST_VIDEO_JSON)


@pytest.fixture
def video():
    return Video(video_id='9lO06Zxhu88')


@pytest.fixture
def video_in_playlist():
    return PLVideo(video_json=PATH_TO_TEST_VIDEO_IN_PLAYLIST_JSON, playlist_json=PATH_TO_VIDEO_IN_PLAYLIST_JSON)


@pytest.fixture
def video_not_playlist():
    return PLVideo(video_json=PATH_TO_TEST_VIDEO_JSON, playlist_json=PATH_TO_VIDEO_NOT_PLAYLIST_JSON)
