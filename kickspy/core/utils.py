import requests
import datetime
import json

 from django.db.models import Q
from random import randint

from .models import Snapshot, Config


def take_snapshot():
    url = Config.objects.filter(key="url").first().value
    data = json.loads(requests.get(url).content)
    date_time = datetime.datetime.now().strftime("%Y%m%d%H%M")
    snapshot = Snapshot(
        url=url,
        date_time=date_time,
        state_changed_at=data["project"]["state_changed_at"],
        state=data["project"]["state"],
        backers_count=data["project"]["backers_count"],
        pledged=data["project"]["pledged"],
        comments_count=data["project"]["comments_count"],
        comments_for_display_count=data["project"]["comments_for_display_count"],
    )
    snapshot.save()


def make_fake_snapshots():
    Snapshot.objects.filter(url="test").delete()
    url = "test"
    backers_count = 0
    comments_count = 0
    pledged = 0
    for day in range(0, 31):
        for hour in range(0, 25):
            for minute in range(0, 61, 7):
                if day < 10:
                    number = get_random_number(day + 1) * 20
                elif day >= 10 and day < 20 :
                    number = get_random_number(day + 1) * 1
                else:
                    number = get_random_number(day + 1) * 60
                if hour > 10 and hour < 14:
                    number = get_random_number(day + 1) * 40
                elif hour > 17 and hour < 23:
                    number = get_random_number(day + 1) * 10
                if day > 14 and day < 16:
                    number = get_random_number(day + 1) * 20
                backers_count += number
                comments_count += number
                pledged += number
                snapshot = Snapshot(
                    url=url,
                    date_time="201901" + ("00" + str(day))[-2:] + ("00" + str(hour))[-2:] + ("00" + str(minute))[-2:],
                    state_changed_at="",
                    state="live",
                    backers_count=str(backers_count),
                    pledged=str(pledged),
                    comments_count=str(backers_count),
                    comments_for_display_count="",
                )
                snapshot.save()


def clear_snapshots():
    url = Config.objects.filter(key="url").first().value
    Snapshot.objects.filter(~Q(url=url)).delete()


def get_random_number(number):
    values = [0, 0, 0, 0, 0, 0, 11, 11, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 99, 7, 9]
    return values[randint(0, len(values) - 1)] * number
