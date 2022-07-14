from api.models import YTVideo 
from rest_framework import serializers



class YTVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YTVideo
        exclude = ['id']