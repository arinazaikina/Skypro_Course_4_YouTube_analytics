import os

import pytest

from youtube import Channel

PATH_TO_TEST_CHANNEL_1_JSON = os.path.join('tests', 'test_channel_1.json')
PATH_TO_TEST_CHANNEL_2_JSON = os.path.join('tests', 'test_channel_2.json')


@pytest.fixture
def channel_1_for_test():
    return Channel(channel_json=PATH_TO_TEST_CHANNEL_1_JSON)


@pytest.fixture
def channel_2_for_test():
    return Channel(channel_json=PATH_TO_TEST_CHANNEL_2_JSON)


@pytest.fixture
def channel():
    return Channel(channel_id='UCMCgOm8GZkHp8zJ6l7_hIuA')
