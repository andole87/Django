import datetime
from haystack import indexes
from .models import Audio

class AudioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document = True, use_template=True,template_name='search/audio_text.txt')
    title = indexes.CharField(model_attr='title')
    
    def get_model(self):
        return Audio

    def index_queryset(self, using=None):
        return self.get_model().objects.all()