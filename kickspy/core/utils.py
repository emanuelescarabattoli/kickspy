import requests
import datetime
import json

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
        for hour in range(0, 24):
            for minute in range(0, 60, 10):
                if day < 10:
                    number = get_random_number(day) * 10
                elif day >= 10 and day < 20 :
                    number = get_random_number(day) * 1
                else:
                    number = get_random_number(day) * 20
                if hour > 10 and hour < 14:
                    number *= 400
                elif hour > 17 and hour < 23:
                    number *= 0.2
                if day > 14 and day < 16:
                    number *= -100
                # number = get_random_number(1)
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


def get_random_number(number):
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 9]
    return values[randint(0, len(values) - 1)] * number
