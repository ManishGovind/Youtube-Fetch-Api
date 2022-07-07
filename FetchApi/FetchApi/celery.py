import os
from celery import Celery


from celery.utils.log import get_task_logger




os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FetchApi.settings")

app = Celery("FetchApi")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


@app.task(bind=True)
def hello_world(self):
    print("Hello world!")


logger = get_task_logger(__name__)


# @app.task(bind=True)
# def update_db(self):
#     """
#     We fetch the latest data from youtube API and add it to your DB.
#     """
#     from youtube_rest_api.models import Video

#     response = youtube_search(SEARCH_QUERY, CHECK_INTV, MAX_RESULTS)
#     logger.info("Successfully Fetched Videos")

#     for item in response.get("items", []):
#         if all(
#             [
#                 not Video.objects.filter(
#                     link=BASE_URL + item["id"]["videoId"]
#                 ).exists(),
#                 item["id"]["kind"] == "youtube#video",
#             ]
#         ):
#             snippet = item["snippet"]
#             video = Video(
#                 video_title=snippet["title"],
#                 description=snippet["description"],
#                 published_on=parser.parse(snippet["publishedAt"]),
#                 thumb_url=snippet["thumbnails"]["default"]["url"],
#                 link=BASE_URL + item["id"]["videoId"],
#             )
#             video.save()
#     logger.info("Successfully Updated Videos DB")
