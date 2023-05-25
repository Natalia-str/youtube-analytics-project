from googleapiclient.discovery import build
import os
import isodate
from datetime import timedelta

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

class PlayList:
    """класс PlayList"""

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.playlist_videos = youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        self.playlists = youtube.playlists().list(
                                             part='snippet',
                                             id=self.__playlist_id,
                                             ).execute()
        self.title = self.playlists['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(self.video_ids)
                                               ).execute()


    @property
    def playlist_id(self):
        """ID """
        return self.__playlist_id

    @property
    def total_duration(self):
        """возвращает объект класса datetime.timedelta с
        суммарной длительность плейлиста"""

        total_time = timedelta(seconds=0)
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            # print(duration)

            total_time = total_time + duration
        return total_time

    def show_best_video(self):
        """возвращает ссылку на самое популярное видео из плейлиста
        (по количеству лайков)
        """
        max_like_count = 0
        max_video_id = 0

        for video in self.video_response['items']:
            like_count: int = video['statistics']['likeCount']
            video_id = video['id']
            if int(like_count) > int(max_like_count):
                max_like_count = like_count
                max_video_id = video_id

        return f'https://youtu.be/{max_video_id}'


# pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
# print(pl.playlist_videos)
# # print(pl.playlists)
# # print(pl.playlist_videos)
# print(pl.total_duration)
# print(pl.show_best_video())
# # print(pl.url)
# # print(pl.title)
# # print(pl.pl)
# print(pl.video_response)