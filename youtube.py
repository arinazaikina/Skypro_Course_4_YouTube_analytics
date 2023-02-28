import json
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build


class Youtube:
    """
    Базовый класс, описывающий объект для работы с API YouTube
    Attrs:
        YOUTUBE_API_KEY (str): ключ для работы с API YouTube
        youtube: клиент для работы с API YouTube
    """
    load_dotenv()
    YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    @staticmethod
    def get_chanel(channel_id):
        channel = Youtube.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return channel

    @staticmethod
    def get_video(video_id):
        video = Youtube.youtube.videos().list(id=video_id, part='snippet,statistics').execute()
        return video

    @staticmethod
    def get_video_in_playlist(video_id, playlist_id):
        video_in_playlist = Youtube.youtube.playlistItems().list(
            part="snippet", playlistId=playlist_id, videoId=video_id
        ).execute()
        return video_in_playlist


class Channel:
    """
    Базовый класс, описывающий YouTube канал
    Attrs:
        channel_id: id YouTube канала
    """

    def __init__(self, channel_id=None, channel_json=None) -> None:
        """
        Инициализируется по id канала или по пути к файлу json (для тестирования)
        Во время создания экземпляра инициализируются атрибуты:
        - channel_info: информация о канале
        - title: название канала
        - description: описание канала
        - link: ссылка на канал
        - subscriber_count: количество подписчиков
        - video_count: количество видео
        - view_count: количество просмотров
        :param channel_id: id канала на YouTube
        :type channel_id: str
        :param channel_json: путь к файлу json с информацией о канала
        :type channel_json: str
        """
        if channel_id is not None:
            self.__channel_info = Youtube.get_chanel(channel_id=channel_id)
        elif channel_json is not None:
            with open(channel_json, 'r') as file:
                data = file.read()
                self.__channel_info = json.loads(data)
        else:
            raise Exception('Illegal arguments')

        self.__channel_id = channel_id
        self.__title = self.title
        self.__description = self.description
        self.__link = self.link
        self.__subscriber_count = self.subscriber_count
        self.__video_count = self.video_count
        self.__view_count = self.view_count

    def __repr__(self):
        return f'Channel(channel_id={self.__channel_id})'

    def __str__(self):
        return f'YouTube-канал: {self.__title}'

    def __len__(self) -> int:
        """Возвращает количество подписчиков"""
        return self.__subscriber_count

    def __add__(self, other: 'Channel') -> int:
        """Сложение количества подписчиков двух каналов"""
        if not isinstance(other, Channel):
            raise ArithmeticError('Правый операнд должен быть объектом Channel')
        return self.__subscriber_count + other.__subscriber_count

    def __gt__(self, other: 'Channel') -> bool:
        """
        Возвращает True, если количество подписчиков на канале больше, чем на другом канале.
        Возвращает False, если количество подписчиков на канале меньше, чем на другом канале.
        """
        if not isinstance(other, Channel):
            raise TypeError('Правый операнд должен быть объектом Channel')
        return self.__subscriber_count > other.__subscriber_count

    @property
    def title(self) -> str:
        """Возвращает название канала"""
        channel_title = self.__channel_info.get('items')[0].get('snippet').get('title')
        return channel_title

    @property
    def description(self) -> str:
        """Возвращает описание канала"""
        channel_description = self.__channel_info.get('items')[0].get('snippet').get('description')
        return channel_description

    @property
    def link(self) -> str:
        """Возвращает ссылку на канал"""
        channel_link = self.__channel_info.get('items')[0].get('snippet').get('customUrl')
        return channel_link

    @property
    def subscriber_count(self) -> int:
        """Возвращает количество подписчиков"""
        channel_subscriber = self.__channel_info.get('items')[0].get('statistics').get('subscriberCount')
        return int(channel_subscriber)

    @property
    def video_count(self) -> int:
        """Возвращает количество видео"""
        channel_video = self.__channel_info.get('items')[0].get('statistics').get('videoCount')
        return int(channel_video)

    @property
    def view_count(self) -> int:
        """Возвращает количество просмотров"""
        channel_view = self.__channel_info.get('items')[0].get('statistics').get('viewCount')
        return int(channel_view)

    def print_info(self) -> None:
        """Выводит на экран информацию о канале"""
        print(self.__channel_info)

    def to_json(self) -> None:
        """
        Сохраняет имеющуюся информации по каналу в json-файл
        """
        with open(f'{self.__channel_id}.json', 'w', encoding='utf-8') as file:
            json.dump(self.__channel_info, file, indent='\t')


class Video:
    def __init__(self, video_id=None, video_json=None) -> None:
        """
       Инициализируется по id видео или по пути к файлу json (для тестирования)
       Во время создания экземпляра инициализируются атрибуты:
       - video_info: информация о видео
       - title: название видео
       - view_count: количество просмотров
       - like_count: количество лайков
       :param video_id: id канала видео
       :type video_id: str
       :param video_json: путь к файлу json с информацией о видео
       :type video_json: str
       """
        if video_id is not None:
            self.__video_info = Youtube.get_video(video_id=video_id)
        elif video_json is not None:
            with open(video_json, 'r') as file:
                data = file.read()
                self.__video_info = json.loads(data)
        else:
            raise Exception('Illegal arguments')

        self.__video_id = video_id
        self.__title = self.title
        self.__url = self.url
        self.__view_count = self.view_count
        self.__like_count = self.like_count

    def __repr__(self):
        return f'Video(video_id={self.__video_id})'

    def __str__(self):
        return self.__title

    @property
    def title(self) -> str:
        """Геттер. Возвращает название видео"""
        video_title = self.__video_info.get('items')[0].get('snippet').get('localized').get('title')
        return video_title

    @property
    def url(self) -> str:
        """Геттер. Возвращает ссылку на видео"""
        video_id = self.__video_info.get('items')[0].get('id')
        url = f'https://www.youtube.com/watch?v={video_id}'
        return url

    @property
    def view_count(self) -> str:
        """Геттер. Возвращает количество просмотров"""
        view_count = self.__video_info.get('items')[0].get('statistics').get('viewCount')
        return view_count

    @property
    def like_count(self) -> str:
        """Геттер. Возвращает количество лайков"""
        like_count = self.__video_info.get('items')[0].get('statistics').get('likeCount')
        return like_count


class PLVideo(Video):
    """
    Класс, описывающий видео в плейлисте.
    Родительский класс - Video.
    Инициализируется по id видео или по пути к файлу json (для тестирования)
    Во время создания экземпляра инициализируются атрибуты:
    - playlist_info: информация о плейлисте
    - video_info: информация о видео
    - title: название видео
    - view_count: количество просмотров
    - like_count: количество лайков
    - id_playlist: если указанное видео есть в указанном плейлисте, то в этот
    атрибут будет записано id плейлиста
    :param video_id: id канала видео
    :type video_id: str
    :param video_json: путь к файлу json с информацией о видео
    :type video_json: str
    :param playlist_id: id плейлиста
    :type playlist_id: str
    :param playlist_json: путь к файлу json с информацией о плейлисте
    :type playlist_json: str
    """

    def __init__(self, video_id=None, video_json=None, playlist_id=None, playlist_json=None):
        super().__init__(video_id, video_json)
        if playlist_id is not None and video_id is not None:
            self.__playlist_info = Youtube.get_video_in_playlist(video_id=video_id, playlist_id=playlist_id)
        elif playlist_json is not None and video_json is not None:
            with open(playlist_json, 'r') as file:
                data = file.read()
                self.__playlist_info = json.loads(data)
        else:
            raise Exception('Illegal arguments')

        self.__id_playlist = self.id_playlist

    @property
    def id_playlist(self) -> str:
        if self.__playlist_info['items']:
            id_playlist = self.__playlist_info.get('items')[0].get('snippet').get('playlistId')
            return id_playlist
        return f'Видео "{self.title}" нет в указанном плейлисте'
