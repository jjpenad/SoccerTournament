from django.db import models
from .Player import Player
from django.db.models import Count
from django.db import connection


class TeamManager(models.Manager):
    
    def get_teams(self):
        return super().get_queryset().all()

    def get_team_most_registered_players(self):
        team_counts = Player.objects.filter(team__isnull=False).values('team').annotate(playersCount=Count('id', distinct=True)).latest('playersCount')    
        if team_counts:
            team = super().get_queryset().get(id=team_counts['team'])
            return team
        return None

class Team(models.Model):
    objects = TeamManager()

    name = models.CharField(max_length=100, unique=True)
    flagImage = models.CharField(max_length=1000)
    teamCrest = models.CharField(max_length=1000)

    class Meta:
        db_table = "Team"
        ordering = ['-id']