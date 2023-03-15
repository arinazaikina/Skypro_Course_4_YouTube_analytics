import datetime

import pytest

from youtube import Video


def test_get_attributes(video_from_json):
    """Проверка получения атрибутов экземпляра класса Video"""
    assert video_from_json.title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video_from_json.url == 'https://www.youtube.com/watch?v=9lO06Zxhu88'
    assert video_from_json.view_count == 49345436
    assert video_from_json.like_count == 976215
    assert video_from_json.duration == datetime.timedelta(seconds=11253)


def test_channel_info_attribute_access(video_from_json):
    """Проверка отсутствия доступа на получение атрибута video_info"""
    with pytest.raises(AttributeError):
        video_info = video_from_json.video_info


def test_exception():
    """
    Проверка вызова исключения при инициализации экземпляра
    класса Video без передачи id канала или пути к файлу json
    """
    with pytest.raises(Exception):
        video = Video()


def test_object_name_str(video_from_youtube):
    """Проверка отображения информации об объекте класса Video для пользователя"""
    assert str(video_from_youtube) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'


def test_object_name_repr(video_from_youtube):
    """Проверка отображения информации об объекте класса Channel для разработчика"""
    assert repr(video_from_youtube) == 'Video(video_id=9lO06Zxhu88)'


def test_incorrect_video_id():
    """Проверка атрибутов и методов, если задан некорректный id видео"""
    video = Video(video_id='test')
    assert video.video_id == 'test'
    assert video.title is None
    assert video.url is None
    assert video.view_count is None
    assert video.like_count is None
    assert video.duration is None
