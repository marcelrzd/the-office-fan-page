from django.db import models
from django.db.models import JSONField

# Create your models here.


class Season(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Season {self.number}"


class Episode(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    air_date = models.DateField()
    season_episode_number = models.CharField(max_length=20)
    series_episode_number = models.IntegerField()
    episode_theme = models.CharField(max_length=60, blank=True, null=True)
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name='episodes')
    main_characters = models.ManyToManyField(
        'Character', related_name='main_episodes', blank=True)
    supporting_characters = models.ManyToManyField(
        'Character', related_name='supporting_episodes', blank=True)
    recurring_characters = models.ManyToManyField(
        'Character', related_name='recurring_episodes', blank=True)

    def __str__(self):
        return f"{self.series_episode_number} - {self.title} (Season {self.season.number}, Episode {self.season_episode_number})"


class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    marital = models.CharField(max_length=100, blank=True, null=True)
    job = JSONField(default=dict)
    workplace = JSONField(default=dict)
    first_appearance = models.CharField(max_length=100, blank=True, null=True)
    last_appearance = models.CharField(max_length=100, blank=True, null=True)
    actor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - '+self.actor if self.actor else 'N/A'


class Quote(models.Model):
    id = models.IntegerField(primary_key=True)
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name='quotes')
    quote = models.TextField()

    def __str__(self):
        return str(self.id) + ' - '+self.character.name + ': '+self.quote[:100]
