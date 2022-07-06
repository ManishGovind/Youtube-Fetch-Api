from django.db import models

# Create your models here.
class YTVideo(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    published_at = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=200)
    channel_id = models.CharField(max_length=100)

    def __str__(self):
        return self.video_id

    
