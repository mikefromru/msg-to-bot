from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):

    message = models.CharField(max_length=500, null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message[:10]
