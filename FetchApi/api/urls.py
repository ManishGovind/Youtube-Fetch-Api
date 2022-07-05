from django.urls import path
from . import views
urlpatterns = [
   path("get-videos/", views.VideoList.as_view(), name="List of Uploaded Videos"),
]