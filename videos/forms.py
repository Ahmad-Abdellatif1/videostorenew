from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['MovieTitle', 'Actor1Name', 'Actor2Name', 'DirectorName', 'MovieGenre', 'ReleaseYear']
        widgets = {
            'MovieTitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie title'}),
            'Actor1Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first actor name'}),
            'Actor2Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter second actor name'}),
            'DirectorName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter director name'}),
            'MovieGenre': forms.Select(attrs={'class': 'form-control'}),
            'ReleaseYear': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter release year'}),
        }