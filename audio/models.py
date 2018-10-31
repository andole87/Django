from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

class Audio(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(db_index=True,max_length=20)
    title_speaker_join = models.CharField(max_length=5,null=True)
    speaker = models.CharField(db_index=True,max_length=10)
    title_author = models.CharField(max_length=5)
    imgsrc = models.CharField(max_length=255,null=True)
    fulltitle = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Audio_Detail(models.Model):
    detail_parent = models.ForeignKey(Audio, on_delete = models.CASCADE)
    detail_title = models.CharField(max_length=20)
    detail_author = models.CharField(max_length=20)
    detail_speaker = models.CharField(max_length=20)
    detail_pubdate = models.CharField(max_length=10, null=True)
    detail_title_text = models.TextField(null=True)
    detail_author_text = models.TextField(null=True)
    detail_speaker_text = models.TextField(null=True)
    detail_imgsrc = models.CharField(max_length=255,null=True)
    detail_audiosrc = models.CharField(max_length=255)
    detail_playtime = models.CharField(max_length=10)
    detail_filesize = models.CharField(null=True, max_length=20)
    detail_price = models.DecimalField(max_digits=5, decimal_places=1,blank=True,null=True)
    detail_outline = models.TextField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.detail_title
