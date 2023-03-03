from youtube import PLVideo


def test_get_attributes_when_video_in_playlist(video_in_playlist):
    """
    Проверка получения атрибутов экземпляра класса PLVideo
    для случая, когда указанное видео есть в указанном плейлисте
    """
    assert video_in_playlist.title == 'Пушкин: наше все?'
    assert video_in_playlist.url == 'https://www.youtube.com/watch?v=BBotskuyw_M'
    assert video_in_playlist.view_count == '506269'
    assert video_in_playlist.like_count == '18491'
    assert video_in_playlist.id_playlist == 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'


def test_get_attributes_when_video_not_in_playlist(video_not_playlist):
    """
    Проверка получения атрибутов экземпляра класса PLVideo
    для случая, когда указанное видео есть в указанном плейлисте
    """
    assert video_not_playlist.title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video_not_playlist.url == 'https://www.youtube.com/watch?v=9lO06Zxhu88'
    assert video_not_playlist.view_count == '49332556'
    assert video_not_playlist.like_count == '976161'
    assert video_not_playlist.id_playlist == 'Видео "Как устроена IT-столица мира / ' \
                                             'Russian Silicon Valley (English subs)" нет в указанном плейлисте'


def test_get_video_in_playlist_by_id():
    video = PLVideo(playlist_id='PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD', video_id='BBotskuyw_M')
    assert str(video) == 'Пушкин: наше все?'
