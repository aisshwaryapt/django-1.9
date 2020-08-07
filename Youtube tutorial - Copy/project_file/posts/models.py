from __future__ import unicode_literals
from django.db import models
from django.conf import settings 
from django.urls import reverse

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class postspage(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,models.CASCADE, default=1)
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_location,
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content=models.TextField(blank=True)
    update=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s" %(self.id)


