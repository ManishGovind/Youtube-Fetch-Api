import os
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from FetchApi.settings import (
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    DEVELOPER_KEY, 
)


def youtube_fetch(query, check_int, max_results):
    
    
    try:
        youtube = build(
            YOUTUBE_API_SERVICE_NAME,
            YOUTUBE_API_VERSION,
            developerKey=DEVELOPER_KEY,
        )

        target_ts = (
            datetime.now() - timedelta(days=60)
        ).isoformat() + "Z"

        search_response = (
            youtube.search()
            .list(
                q=query,
                part="snippet",
                maxResults=max_results,
                order="date",
                publishedAfter=target_ts,
            )
            .execute()
        )
        print(f"Request Succeeded with API_KEY")
        return search_response
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
        if e.resp.status == 403:
            print(f"Request Failed with API_KEY")
            # get_next_key()
        return dict()
