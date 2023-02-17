import os

import pytest

from youtube import Channel

PATH_TO_TEST_CHANNEL_JSON = os.path.join('tests', 'test_channel.json')


@pytest.fixture
def channel_for_test():
    return Channel(channel_json=PATH_TO_TEST_CHANNEL_JSON)


@pytest.fixture
def channel():
    return Channel(channel_id='UCMCgOm8GZkHp8zJ6l7_hIuA')
