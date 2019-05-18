from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import StatsView, SnapshotView, FakeSnapshotsView


urlpatterns = [
    path("stats", StatsView.as_view(), name="stats"),
    path("snapshot", SnapshotView.as_view(), name="snapshot"),
    path("fake-snapshots", FakeSnapshotsView.as_view(), name="fake_snapshots"),
]
