from SoccerTournamentApp.models import TechnicalStaff

def get_technicalStaff():
    ''' Returns the players participating in the tournament '''
    return TechnicalStaff.objects.get_technicalStaff()

def get_oldest_tecnicalStaff():
    ''' Returns the oldest player participating in the tournament '''
    return TechnicalStaff.objects.get_oldest_tecnicalStaff()