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

