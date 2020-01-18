from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):   #models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  #this is a link to another model.
    title = models.CharField(max_length=200)    #limited length
    text = models.TextField()   #unlimited length
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):      #with this method we get a text (string) with a Post title.
        return self.title
