import os.path

import pytest

from youtube import Channel


def test_get_attributes(channel_1_for_test):
    assert channel_1_for_test.title == 'вДудь'
    assert channel_1_for_test.description == 'Здесь задают вопросы'
    assert channel_1_for_test.link == '@vdud'
    assert channel_1_for_test.subscriber_count == 10300000
    assert channel_1_for_test.video_count == 164
    assert channel_1_for_test.view_count == 1946788891


def test_channel_info_attribute_access(channel_1_for_test):
    with pytest.raises(AttributeError):
        channel_info = channel_1_for_test.channel_info


def test_change_attributes_access(channel_1_for_test):
    with pytest.raises(AttributeError):
        channel_1_for_test.title = 'new'
        channel_1_for_test.description = 'new'
        channel_1_for_test.link = 'new'
        channel_1_for_test.subscriber_count = 'new'
        channel_1_for_test.video_count = 'new'
        channel_1_for_test.view_count = 'new'


def test_exception():
    with pytest.raises(Exception):
        channel = Channel()


def test_object_name_str(channel):
    assert str(channel) == 'YouTube-канал: вДудь'


def test_object_name_repr(channel):
    assert repr(channel) == 'Channel(channel_id=UCMCgOm8GZkHp8zJ6l7_hIuA)'


def test_to_json(channel_1_for_test):
    channel_1_for_test.to_json()
    file_path = 'None.json'
    os.path.exists(file_path)
    os.remove(file_path)


def test_len(channel_1_for_test):
    assert len(channel_1_for_test) == 10300000


def test_add(channel_1_for_test, channel_2_for_test):
    assert channel_1_for_test + channel_2_for_test == 13980000


def test_gt(channel_1_for_test, channel_2_for_test):
    assert channel_1_for_test > channel_2_for_test
    assert channel_2_for_test < channel_1_for_test
