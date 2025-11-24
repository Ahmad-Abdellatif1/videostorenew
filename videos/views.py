from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Video
from .forms import VideoForm

def home(request):
    """Home page - display all videos"""
    videos = Video.objects.all()
    return render(request, 'videos/home.html', {'videos': videos})

def add_video(request):
    """Add a new video"""
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'videos/add_video.html', {'form': form})

def view_video(request, movie_id):
    """View details of a specific video"""
    video = get_object_or_404(Video, MovieID=movie_id)
    return render(request, 'videos/view_video.html', {'video': video})

def update_video(request, movie_id):
    """Update an existing video"""
    video = get_object_or_404(Video, MovieID=movie_id)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm(instance=video)
    return render(request, 'videos/update_video.html', {'form': form, 'video': video})

def delete_video(request, movie_id):
    """Delete a video"""
    video = get_object_or_404(Video, MovieID=movie_id)
    if request.method == 'POST':
        video.delete()
        return redirect('home')
    return render(request, 'videos/delete_video.html', {'video': video})