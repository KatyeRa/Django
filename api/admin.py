from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Track, Playlist, Album


@admin.register(Track)
class TrackAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True


@admin.register(Playlist)
class PlaylistAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True


@admin.register(Album)
class AlbumAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True
