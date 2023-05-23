from googleapiclient.discovery import build
import os


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

class PlayList:
    """класс PlayList"""

    def __init__(self, playlist_id):
        pass