import datetime

import pytest

from youtube import PlayList


def test_get_attributes(playlist_from_json, ):
    """Проверка получения атрибутов экземпляра класса Playlist"""
    assert playlist_from_json.title == '[Вся правда о НАТО]'
    assert playlist_from_json.url == 'https://www.youtube.com/playlist?list=None'


def test_playlist_info_attribute_access(playlist_from_json):
    """Проверка отсутствия доступа на получение атрибута video_info"""
    with pytest.raises(AttributeError):
        playlist_info = playlist_from_json.playlist_info


def test_exception():
    """
    Проверка вызова исключения при инициализации экземпляра
    класса PlayList без передачи id плейлиста или пути к файлу json
    """
    with pytest.raises(Exception):
        video = PlayList()


def test_object_name_str(playlist_from_youtube):
    """Проверка отображения информации об объекте класса Video для пользователя"""
    assert str(playlist_from_youtube) == 'YouTube-плейлист: Редакция. АнтиТревел'


def test_object_name_repr(playlist_from_youtube):
    """Проверка отображения информации об объекте класса PlayList для разработчика"""
    assert repr(playlist_from_youtube) == 'PlayList(playlist_id=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb)'


def test_duration(playlist_from_youtube):
    """Проверка длительности плейлиста"""
    duration = playlist_from_youtube.total_duration
    assert duration == datetime.timedelta(seconds=13261)


def test_show_best_video(playlist_from_youtube):
    """Проверка популярного видео в плейлисте"""
    assert playlist_from_youtube.show_best_video() == 'https://www.youtube.com/watch?v=9Bv2zltQKQA'


def test_incorrect_playlist_id():
    """Проверка атрибутов и методов, если задан некорректный id плейлиста"""
    playlist = PlayList(playlist_id='test')
    assert playlist.playlist_id == 'test'
    assert playlist.title is None
    assert playlist.url is None
    assert playlist.total_duration == datetime.timedelta(0)
    assert playlist.show_best_video() is None
