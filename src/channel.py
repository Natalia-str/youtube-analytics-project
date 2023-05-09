import json
import os
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


    @property
    def channel_id(self):
        """ID канала"""
        return self.__channel_id

    @property
    def title(self):
        """название канала"""
        return self.channel["items"][0]["snippet"]["title"]

    @property
    def description(self):
        """описание канала"""
        return self.channel["items"][0]["snippet"]["description"]

    @property
    def url(self):
        """ссылка на канал"""
        return f"https://www.youtube.com/channel/{self.__channel_id}"


    @property
    def subscriber_count(self):
        """количество подписчиков"""
        return self.channel["items"][0]["statistics"]["subscriberCount"]

    @property
    def view_count(self):
        """общее количество просмотров"""
        return self.channel["items"][0]["statistics"]["viewCount"]

    @property
    def video_count(self):
        """количество видео"""
        return self.channel["items"][0]["statistics"]["videoCount"]

    @classmethod
    def get_service(cls):
        pass

    def to_json(self):
        """сохраняет в файл значения атрибутов экземпляра Channel"""
        info = {'ID канала': self.__channel_id,
                 'название канала': self.title,
                 'описание канала': self.description,
                 'ссылка на канал': self.url,
                 'количество подписчиков': self.subscriber_count,
                 'общее количество просмотров': self.view_count,
                 'количество видео': self.video_count}

        info_1 = json.dumps(info)

        py_info = json.loads(info_1)

        with open('data_channel.json', 'w', encoding='utf-8') as f:
            json.dump(py_info, f, indent=2, ensure_ascii=False)




    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info = json.dumps(self.channel, indent=2, ensure_ascii=False)
        return print(info)

vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
print(vdud.title)
print(vdud.channel_id)
print(vdud.url)
print(vdud.video_count)
print(vdud.description)
print(vdud.to_json())
