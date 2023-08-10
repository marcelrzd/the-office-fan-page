from django.db import models

# Create your models here.
class Season(models.Model):
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
    episode_number = models.IntegerField()
    series_episode_number = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    main_characters = models.ManyToManyField('Character', related_name='main_episodes', blank=True)
    supporting_characters = models.ManyToManyField('Character', related_name='supporting_episodes', blank=True)
    recurring_characters = models.ManyToManyField('Character', related_name='recurring_episodes', blank=True)

    def __str__(self):
        return f"{self.title} (Season {self.season.number}, Episode {self.episode_number})"

class Character(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    marital = models.CharField(max_length=20, blank=True, null=True)
    job = models.ManyToManyField('Job', related_name='characters', blank=True)
    workplace = models.ManyToManyField('Workplace', related_name='characters', blank=True)
    first_appearance = models.CharField(max_length=100, blank=True)
    last_appearance = models.CharField(max_length=100, blank=True)
    actor = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title +' - '+self.actor

class Workplace(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name