from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
import django_filters.rest_framework
from api.serializers import AlbumSerializer, PlaylistSerializer, TrackSerializer
from .models import Album, Playlist, Track


class TrackViewSet(ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.filter(Q(is_visible=True))
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name',]


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class PlaylistViewSet(ModelViewSet):
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()