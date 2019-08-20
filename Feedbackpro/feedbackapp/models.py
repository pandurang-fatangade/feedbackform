from django.db import models

class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField(max_length=200)
    feedback=models.TextField(max_length=200)
