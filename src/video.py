from googleapiclient.discovery import build
import os
import json
import isodate


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    """класс Video"""

    def __init__(self, id_video):
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.__id_video = id_video
        try:
            self.video = youtube.videos().list(id=id_video, part='snippet,statistics').execute()
            self.video["items"][0] is None
        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

        else:
            self.title = self.video["items"][0]["snippet"]["title"]
            self.url = f"https://www.youtube.com/video/{self.__id_video}"
            self.view_count = self.video["items"][0]["statistics"]["viewCount"]
            self.like_count = self.video["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return self.title

    @property
    def id_video(self):
        """ID """
        return self.__id_video

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info = json.dumps(self.video, indent=2, ensure_ascii=False)
        return print(info)

class PLVideo(Video):
    """класс PLVideo"""
    def __init__(self, id_video, id_playlist):
        """Экземпляр инициализируется id видео и id плейлиста. Дальше все данные будут подтягиваться по API."""
        super().__init__(id_video)
        self.id_playlist = id_playlist
        self.playlist_videos = youtube.playlistItems().list(playlistId=id_playlist,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()



# video1 = Video('9lO06Zxhu88')  # '9lO06Zxhu88' - это id видео из ютуб
# # # video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
# # print(video1.id_video)
# # video1.print_info()
# # print(video1.video)
# print(video1.url)
# print(video1.view_count)
# print(video1.like_count)