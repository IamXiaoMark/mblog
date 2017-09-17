from django.db import models
from django.utils import timezone

# Create your models here.

#继承至Model
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200) #网址
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now) #发表时间

    class Meta: #指定文章显示的顺序是以pub_date为依据
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title