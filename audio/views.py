from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Audio

# Create your views here.

def audio_list(request):
    audios = Audio.objects.order_by('audiosrc')
    return render(request, 'audio/audio_list.html', {'audios':audios})

def audio_detail(request, pk):
    audio = get_object_or_404(Audio, pk=pk)
    return render(request, 'audio/audio_detail.html', {'audio':audio})


