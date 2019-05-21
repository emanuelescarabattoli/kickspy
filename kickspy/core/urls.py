from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import StatsView, SnapshotView, FakeSnapshotsView, DailyView, DiffView, ClearSnapshotsView, LiveView, LiveJsonView, DaysView, CsvView


urlpatterns = [
    path("stats", StatsView.as_view(), name="stats"),
    path("days", DaysView.as_view(), name="days"),
    path("live", LiveView.as_view(), name="live"),
    path("live-json", LiveJsonView.as_view(), name="live"),
    path("csv", CsvView.as_view(), name="csv"),
    path("daily", DailyView.as_view(), name="daily"),
    path("diff", DiffView.as_view(), name="daily"),
    path("snapshot", SnapshotView.as_view(), name="snapshot"),
    path("fake-snapshots", FakeSnapshotsView.as_view(), name="fake_snapshots"),
    path("clear-snapshots", ClearSnapshotsView.as_view(), name="clear_snapshots"),
]
