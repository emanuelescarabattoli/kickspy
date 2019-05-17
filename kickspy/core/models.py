from django.db import models


class Snapshot(models.Model):
    url = models.CharField(max_length=512)
    date_time = models.CharField(max_length=512)
    state_changed_at = models.CharField(max_length=512)
    state = models.CharField(max_length=512)
    backers_count = models.CharField(max_length=512)
    pledged = models.CharField(max_length=512)
    comments_count = models.CharField(max_length=512)
    comments_for_display_count = models.CharField(max_length=512)


class Config(models.Model):
    key = models.CharField(max_length=512)
    value = models.CharField(max_length=512)
