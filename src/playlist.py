from googleapiclient.discovery import build
import os
import json
import requests

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

class PlayList:
    """класс PlayList"""

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        # self.playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
        #                                                part='contentDetails',
        #                                                maxResults=50,
        #                                                ).execute()
        self.playlists = youtube.playlists().list(
                                             part='snippet',
                                             id=playlist_id,
                                             ).execute()
        # self.title = self.playlists['items']['snippet']['title']
        self.title = self.playlists['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"
        # self.title = self.playlist_videos[]
        # self.response = requests.get(https://www.googleapis.com/youtube/v3/playlists)


    @property
    def playlist_id(self):
        """ID """
        return self.__playlist_id

pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(pl.playlists)
print(pl.url)
print(pl.title)
# print(pl.pl)
# print(pl.response.content)