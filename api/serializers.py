from rest_framework.serializers import ModelSerializer
from .models import Track, Album, Playlist


class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class PlaylistSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
