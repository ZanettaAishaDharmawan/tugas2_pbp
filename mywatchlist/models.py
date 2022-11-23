from logging.handlers import WatchedFileHandler
from django.db import models

# Create your models here.
class MyWatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.CharField(max_length=255)