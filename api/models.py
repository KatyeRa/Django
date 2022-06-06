from django.db import models
from simple_history.models import HistoricalRecords

class Track(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    audio_file = models.FileField(verbose_name='Аудио', upload_to='tracks')
    image = models.ImageField(verbose_name='Обложка', upload_to='img/covers')
    is_visible = models.BooleanField(verbose_name='Виден?', default=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

class Playlist(models.Model):
    name = models.CharField(verbose_name='Название плейлиста', max_length=255)
    description = models.TextField(verbose_name='Описание плейлиста')
    tracks = models.ManyToManyField(Track, verbose_name='Треки')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Плейлист'
        verbose_name_plural = 'Плейлисты'

class Album(models.Model):
    name = models.CharField(verbose_name='Название альбома', max_length=255)
    description = models.TextField(verbose_name='Описание альбома')
    tracks = models.ManyToManyField(Track, verbose_name='Треки')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
