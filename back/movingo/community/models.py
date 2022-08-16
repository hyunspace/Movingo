from django.db import models
from django.conf import settings
from movies.models import Movie
from datetime import datetime, timedelta, timezone

# Create your models here.
class Thread(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __self__(self):
        return self.movie
    
class Comment(models.Model):
    thread = models.ForeignKey(Thread, related_name="comments", on_delete= models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def created_string(self):
            time = datetime.now(tz=timezone.utc) - self.created_at
            if time < timedelta(minutes=1):
                return '방금 전'
            elif time < timedelta(hours=1):
                return str(int(time.seconds / 60)) + '분 전'
            elif time < timedelta(days=1):
                return str(int(time.seconds / 3600)) + '시간 전'
            elif time < timedelta(days=7):
                time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
                return str(time.days) + '일 전'
            else:
                return self.created_at.date
    def __self__(self):
        return self.content