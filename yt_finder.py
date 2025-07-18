# youtube_finder.py

import datetime
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube_videos(query):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    published_after = (datetime.datetime.utcnow() - datetime.timedelta(days=14)).isoformat("T") + "Z"

    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=20,
        publishedAfter=published_after,
        videoDuration='medium'  # 4-20 mins
    )
    response = request.execute()

    videos = []
    for item in response['items']:
        videos.append({
            'title': item['snippet']['title'],
            'videoId': item['id']['videoId'],
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        })

    return videos
