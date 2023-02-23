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


class Channel:
    """
    Базовый класс, описывающий YouTube канал
    Attrs:
        channel_id: id YouTube канала
    """

    def __init__(self, channel_id=None, channel_json=None):
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
