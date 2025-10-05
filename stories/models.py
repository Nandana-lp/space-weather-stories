from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='story_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NasaAPOD(models.Model):
    date = models.DateField(unique=True)
    title = models.CharField(max_length=250)
    explanation = models.TextField()
    url = models.URLField()  # image/video URL
    media_type = models.CharField(max_length=20)  # 'image' or 'video'

    def __str__(self):
        return f"{self.date} - {self.title}"
