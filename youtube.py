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


class Channel:
    """
    Базовый класс, описывающий YouTube канал
    Attrs:
        channel_id (str): id YouTube канала
    """

    def __init__(self, channel_id):
        self.__channel_id = channel_id

    def __repr__(self):
        return repr(f'Channel(channel_id={self.__channel_id})')

    def __str__(self):
        return f'YouTube channel {self.get_channel_title()} id={self.__channel_id}'

    def get_channel(self) -> dict:
        """Возвращает информацию о канале"""
        channel = Youtube.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    def get_channel_title(self) -> str:
        """Возвращает название канала"""
        channel = self.get_channel()
        channel_title = channel.get('items')[0].get('snippet').get('title')
        return channel_title

    def print_info(self) -> None:
        """Выводит на экран информацию о канале"""
        print(self.get_channel())
