from django.db import models
from django.db.models import Count, Avg, F, ExpressionWrapper
from datetime import date, timedelta

POSITION_CHOICES = [
        ('Goalkeeper', 'Goalkeeper'),
        ('Full-Back', 'Full-Back'),
        ('Wing-Back', 'Wing-Back'),
        ('Central Defender', 'Central Defender'),
        ('Sweeper', 'Sweeper'),
        ('Central Midfield', 'Central Midfield'),
        ('Wide Midfield', 'Wide Midfield'),
        ('Striker', 'Striker'),
        ('Behind The Striker', 'Behind The Striker')
    ]

class PlayerManager(models.Manager):

    def get_players(self):
        return super().get_queryset().all()

    def get_players_count(self):
        return super().get_queryset().all().count()

    def get_youngest_player(self):
        return super().get_queryset().order_by('-birthDate').first()

    def get_oldest_player(self):
        return super().get_queryset().order_by('birthDate').first()

    def get_substitute_players(self):
        return super().get_queryset().filter(firstEleven=False)

    def get_substitute_players_count(self):
        return super().get_queryset().filter(firstEleven=False).count()

    def get_substitute_players_count(self):
        return super().get_queryset().filter(firstEleven=False).count()

    def average_substitutes_per_team(self):
        team_counts = super().get_queryset().filter(team__isnull=False, firstEleven=False).values('team').annotate(Count('id', distinct=True))
        if team_counts.exists():
            average = team_counts.aggregate(Avg('id__count'))
            return int(average["id__count__avg"])

        return 0

    def average_players_per_team(self):
        team_counts = super().get_queryset().filter(team__isnull=False).values('team').annotate(Count('id', distinct=True))
        if team_counts.exists():
            average = team_counts.aggregate(Avg('id__count'))
            return int(average["id__count__avg"])

        return 0

    def average_players_age(self):
        '''Return the average age of the players in years'''
        age_expression = ExpressionWrapper((date.today()-F('birthDate')), output_field=models.DurationField())
        # Return the average in days and seconds
        players_age = super().get_queryset().annotate(age = age_expression).aggregate(Avg('age'))
        seconds_in_year = 365.25*24*60*60
        average_age = players_age['age__avg'].total_seconds()/seconds_in_year
        return int(average_age)

class Player(models.Model):
    objects=PlayerManager()

    photo = models.CharField(max_length=1000)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDate = models.DateField()
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    shirtNumber = models.IntegerField()
    firstEleven = models.BooleanField()

    # Relationships
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        related_name='players'
    )

    class Meta:
        db_table = "Player"
