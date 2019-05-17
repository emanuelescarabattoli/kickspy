import requests
import datetime
import json

from django.core.management.base import BaseCommand, CommandError
from ...models import Snapshot, Config


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = Config.objects.filter(key="url").first().value
        data = json.loads(requests.get(url).content)
        date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
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
