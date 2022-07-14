import os
import requests
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from FetchApi.settings import DEVELOPER_KEY

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'



def youtube_fetch(query,max_results):
    
    
    try:
        youtube = build(
            YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY,
        )

        published_date = (
            datetime.now() - timedelta(days=60)
        ).isoformat() + "Z"

        search_response = (
            youtube.search()
            .list(
                q=query,
                part="snippet",
                maxResults=max_results,
                order="date",
                publishedAfter=published_date,
            )
            .execute()
        )
        print(f"Request Succeeded with API_KEY")
        return search_response
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
        if e.resp.status == 403:
            print(f"Request Failed with API_KEY")
        return dict()
