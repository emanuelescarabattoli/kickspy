import requests
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .utils import take_snapshot, make_fake_snapshots, clear_snapshots
from .models import Snapshot, Config


class StatsView(LoginRequiredMixin, View):

    template = "stats.html"

    def get(self, request, *args, **kwargs):
        url = Config.objects.filter(key="url").first().value
        stats = json.dumps(list(Snapshot.objects.filter(url=url).order_by("date_time").values()))
        return render(request, self.template, {"stats": stats})


class DaysView(LoginRequiredMixin, View):

    template = "days.html"

    def get(self, request, *args, **kwargs):
        url = Config.objects.filter(key="url").first().value
        stats = json.dumps(list(Snapshot.objects.filter(url=url).order_by("date_time").values()))
        return render(request, self.template, {"stats": stats})


class LiveView(LoginRequiredMixin, View):

    template = "live.html"

    def get(self, request, *args, **kwargs):
        goal = Config.objects.filter(key="goal").first().value
        return render(request, self.template, {"goal": goal})


class DiffView(LoginRequiredMixin, View):

    template = "diff.html"

    def get(self, request, *args, **kwargs):
        url = Config.objects.filter(key="url").first().value
        stats = json.dumps(list(Snapshot.objects.filter(url=url).order_by("date_time").values()))
        return render(request, self.template, {"stats": stats})

class DailyView(LoginRequiredMixin, View):

    template = "daily.html"

    def get(self, request, *args, **kwargs):
        url = Config.objects.filter(key="url").first().value
        stats = json.dumps(list(Snapshot.objects.filter(url=url).order_by("date_time").values()))
        return render(request, self.template, {"stats": stats})


class SnapshotView(View):

    def get(self, request, *args, **kwargs):
        take_snapshot()
        return JsonResponse({ "total_snapshots": Snapshot.objects.count() })


class LiveJsonView(View):

    def get(self, request, *args, **kwargs):
        url = Config.objects.filter(key="url").first().value
        data = json.loads(requests.get(url).content)
        return JsonResponse({ "data": data })


class FakeSnapshotsView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        make_fake_snapshots()
        return JsonResponse({ "total_snapshots": Snapshot.objects.count() })


class ClearSnapshotsView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        clear_snapshots()
        return JsonResponse({ "total_snapshots": Snapshot.objects.count() })