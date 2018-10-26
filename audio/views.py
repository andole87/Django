from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Audio
from .models import Audio_Detail

# Create your views here.

def audio_list(request):
    audios = Audio.objects.order_by('id')
    return render(request, 'audio/audio_list.html', {'audios':audios})

def audio_detail(request, i):
    details = Audio_Detail.objects.get(detail_parent_id = i)
    return render(request, 'audio/audio_detail.html', {'details':details})

def audio_search(request, title):
    audio = Audio.objects.filter(title__contains=title).union(Audio.objects.filter(speaker__contains=title))
    return render(request, 'audio/audio_list.html', {'audios':audio})
