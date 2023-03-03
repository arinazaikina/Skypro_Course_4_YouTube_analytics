import pytest

from youtube import Video


def test_get_attributes(video_for_test):
    """Проверка получения атрибутов экземпляра класса Video"""
    assert video_for_test.title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video_for_test.url == 'https://www.youtube.com/watch?v=9lO06Zxhu88'
    assert video_for_test.view_count == '49332556'
    assert video_for_test.like_count == '976161'


def test_channel_info_attribute_access(video_for_test):
    """Проверка отсутствия доступа на получение атрибута video_info"""
    with pytest.raises(AttributeError):
        video_info = video_for_test.video_info


def test_exception():
    """
    Проверка вызова исключения при инициализации экземпляра
    класса Video без передачи id канала или пути к файлу json
    """
    with pytest.raises(Exception):
        video = Video()


def test_object_name_str(video):
    """Проверка отображения информации об объекте класса Video для пользователя"""
    assert str(video) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'


def test_object_name_repr(video):
    """Проверка отображения информации об объекте класса Channel для разработчика"""
    assert repr(video) == 'Video(video_id=9lO06Zxhu88)'
