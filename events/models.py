from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    reg = models.URLField()
    description = models.TextField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    orgzer = models.CharField(max_length=100)
    winners = models.TextField(blank=True, default='Not Yet Decided')
    # poster = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    #member_exclusive = models.BooleanField(default=None, blank=True)
    is_approved = models.BooleanField(default=False, blank=True)
    approved_by = models.CharField(
        max_length=40,  null=True, blank=True, default=" ")
    # likes = models.ManyToManyField(User, related_name="like_event")

    def __str__(self):
        return self.event_name

    def snippet(self):
        return self.description[:10] + '...'

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class Update(models.Model):
    title = models.CharField(max_length=50, blank=True)
    Update = models.TextField(max_length=250)
    created = models.DateField(auto_now_add=True)
    till_when = models.DateField()
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Update'
        verbose_name_plural = 'Announcements'
