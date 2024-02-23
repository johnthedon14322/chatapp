from django.db import models
from datetime import datetime
# Create your models here.

class Messages(models.Model):

    user = models.CharField(max_length=20)
    message = models.TextField()
    seened = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        date  = datetime.date(self.created_at).strftime("%h:%m")
        time  = datetime.time(self.created_at).strftime("%H:%M")
        return self.user + " - " + self.message  + "," + date + ", "+ time