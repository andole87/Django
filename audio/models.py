from django.db import models
from django.utils import timezone
# Create your models here.

class Audio(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(db_index=True,max_length=20)
    speaker = models.CharField(db_index=True,max_length=10)
    audiosrc = models.CharField(max_length=255)
    imgsrc = models.CharField(max_length=255,null=True)
    text = models.TextField()
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
    detail_translator = models.CharField(blank=True, null=True, max_length=20)
    detail_speaker = models.CharField(max_length=20)
    detail_pubdate = models.DateTimeField(blank=True, null=True)
    detail_text = models.TextField()
    detail_imgsrc = models.CharField(max_length=255)
    detail_playtime = models.TimeField(blank=True)
    detail_filesize = models.CharField(null=True, max_length=20)
    detail_price = models.DecimalField(max_digits=5, decimal_places=1,blank=True,null=True)
    detail_outline = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.detail_title

    

