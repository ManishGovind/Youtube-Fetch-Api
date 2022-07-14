from datetime import datetime
from threading import Thread
from celery import shared_task
from celery.utils.log import get_task_logger
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from api.models import YTVideo 
from api.utils import youtube_fetch
from FetchApi.settings import SEARCH_QUERY , MAX_RESULTS


logger = get_task_logger(__name__)


@shared_task(bind=True)
def save_videos(*args):
    """
    fetch the latest data from youtube API and add it to DB.
    """
    response = youtube_fetch(SEARCH_QUERY, MAX_RESULTS)
    logger.info("Successfully Fetched Videos")

    for item in response.get("items", []):
        if all(
            [
                not YTVideo.objects.filter(
                    video_id = item["id"]["videoId"]
                ).exists(),
                item["id"]["kind"] == "youtube#video",
            ]
        ):
        
            YTVideo.objects.create(
            title=item['snippet']['title'],
            video_id = item['id']['videoId'],
            channel_id = item['snippet']['channelId'],
            description = item['snippet']['description'],
            published_at=datetime.strptime((item['snippet']['publishedAt'][:-1]), "%Y-%m-%dT%H:%M:%S"),
            thumbnail_url=item['snippet']['thumbnails']['default']['url'],

        )
    logger.info("Videos uploaded in to db successfully")


    




