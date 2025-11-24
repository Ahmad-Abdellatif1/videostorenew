from django.db import models

class Video(models.Model):
    MovieID = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=100)
    Actor2Name = models.CharField(max_length=100)
    DirectorName = models.CharField(max_length=100)
    
    GENRE_CHOICES = [
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),
    ]
    
    MovieGenre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    ReleaseYear = models.IntegerField()
    
    def __str__(self):
        return self.MovieTitle
    
    class Meta:
        db_table = 'videos'
        ordering = ['-ReleaseYear']