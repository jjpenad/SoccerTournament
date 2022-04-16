from rest_framework import viewsets
from rest_framework.decorators import action
from SoccerTournamentApp.logic.Team import *
from SoccerTournamentApp.models import Team
from SoccerTournamentApp.api.Serializers import TeamSerializer
from rest_framework.response import Response

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        teams = get_teams()
        serializer_context = {
            'request': request,
        }
        serializer = TeamSerializer(teams, context=serializer_context, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='stats/total-count', url_name='stats_count')
    def get_total_count(self, request, pk=None):
        all_teams_count = Team.objects.all().count()
        return Response(all_teams_count)

    
    @action(methods=['get'], detail=False, url_path='stats/team-most-registered-players', url_name='team_most_registered_players')
    def get_team_most_registered_players(self, request):
        team = team_most_registered_players()
        serializer_context = {
            'request': request,
        }
        serializer = TeamSerializer(team, context=serializer_context, many=False)
        return Response(serializer.data)