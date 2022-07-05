from django.urls import path
from . import views
urlpatterns = [
   path("get-videos/", views.getVideos.as_view(), name="List of Uploaded Videos"),
]