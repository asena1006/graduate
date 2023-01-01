from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="selling/post/%Y/%m/%d")
    caption = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse("selling:post_detail", args=[self.pk])
