from rest_framework import generics
from api.models import YTVideo
from api.serializers import YTVideoSerializer
from django_filters.rest_framework import DjangoFilterBackend




# Create your views here.
class VideoList(generics.ListAPIView):
    queryset = YTVideo.objects.order_by("-published_at")
    serializer_class = YTVideoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'published_at']
    