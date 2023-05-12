import json
import os
import requests
from googleapiclient.discovery import build

import isodate

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


# channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["videoCount"]

    def __str__(self):
        return f'{self.title} ({self.url})'

    @property
    def channel_id(self):
        """ID канала"""
        return self.__channel_id

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self):
        """сохраняет в файл значения атрибутов экземпляра Channel"""
        info = self.__dict__
        with open('data_channel.json', 'w', encoding='utf-8') as f:
            json.dump(info, f, indent=2, ensure_ascii=False)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info = json.dumps(self.channel, indent=2, ensure_ascii=False)
        return print(info)


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
# print(vdud.title)
# print(vdud.channel_id)
# print(vdud.url)
# print(vdud.video_count)
# print(vdud.description)
# print(vdud.to_json())
# print(Channel.get_service())
print(vdud)
