from SoccerTournamentApp.models import Team

def get_teams():
    ''' Returns the teams participating in the tournament '''
    return Team.objects.get_teams()


def team_most_registered_players():
    ''' Returns the team with most players registered in the tournament '''
    return Team.objects.get_team_most_registered_players()