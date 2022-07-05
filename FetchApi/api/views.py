from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
# from api.models import VideoModel
# from api.serializers import VideoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# Create your views here.
class VideoList(generics.ListAPIView):
    print("hello world")