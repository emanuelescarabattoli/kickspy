from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import StatsView, SnapshotView, FakeSnapshotsView, DailyView


urlpatterns = [
    path("stats", StatsView.as_view(), name="stats"),
    path("daily", DailyView.as_view(), name="daily"),
    path("snapshot", SnapshotView.as_view(), name="snapshot"),
    path("fake-snapshots", FakeSnapshotsView.as_view(), name="fake_snapshots"),
]
