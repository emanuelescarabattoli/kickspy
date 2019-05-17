from django.contrib import admin

from .models import Snapshot, Config


admin.site.register(Snapshot)
admin.site.register(Config)
