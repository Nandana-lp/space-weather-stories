from django.shortcuts import render
from .models import Story
from .utils import fetch_nasa_apod


def story_detail(request, pk):
    story = Story.objects.get(pk=pk)
    return render(request, 'stories/story_detail.html', {'story': story})

def story_list(request):
    apod = fetch_nasa_apod()  # Fetch NASA APOD
    stories = Story.objects.all().order_by('-created_at')
    return render(request, 'stories/story_list.html', {'stories': stories, 'apod': apod})
