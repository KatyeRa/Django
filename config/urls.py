from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import UserViewSet
from api.views import TrackViewSet, PlaylistViewSet, AlbumViewSet


def trigger_error(request):
    division_by_zero = 1 / 0

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('track', TrackViewSet)
router.register('playlist', PlaylistViewSet)
router.register('album', AlbumViewSet)


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)