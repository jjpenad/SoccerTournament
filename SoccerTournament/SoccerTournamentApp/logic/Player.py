from SoccerTournamentApp.models import Player

def get_players():
    ''' Returns the players participating in the tournament '''
    return Player.objects.get_players()


def get_players_count():
    ''' Returns how many players are participating in the tournament '''
    return Player.objects.get_players_count()

def get_youngest_player():
    ''' Returns the youngest player participating in the tournament '''
    return Player.objects.get_youngest_player()

def get_oldest_player():
    ''' Returns the oldest player participating in the tournament '''
    return Player.objects.get_oldest_player()

def get_substitute_players():
    ''' Returns the substitute players participating in the tournament '''
    return Player.objects.get_substitute_players()

def get_substitute_players_count():
    ''' Returns the amount of substitute players participating in the tournament '''
    return Player.objects.get_substitute_players_count()

def average_substitutes_per_team():
    ''' Returns the average quantity of substitute players participating in the tournament per team'''
    return Player.objects.average_substitutes_per_team()

def average_players_per_team():
    ''' Returns the average quantity of substitute players participating in the tournament per team'''
    return Player.objects.average_players_per_team()

def average_players_age():
    ''' Returns the average age of the players participating in the tournament'''
    return Player.objects.average_players_age()