from rest_framework import viewsets
from rest_framework.decorators import action
from SoccerTournamentApp.models import Player
from SoccerTournamentApp.logic.Player import *
from SoccerTournamentApp.api.Serializers import PlayerSerializer
from rest_framework.response import Response

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        players = get_players()
        serializer_context = {
            'request': request,
        }
        serializer = PlayerSerializer(players, context=serializer_context, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='stats/total-count', url_name='stats_count')
    def get_total_count(self, request, pk=None):
        count = get_players_count()
        return Response(count)

    @action(methods=['get'], detail=False, url_path='stats/youngest-player', url_name='youngest_player')
    def get_youngest_player(self, request):
        youngest_player = get_youngest_player()
        serializer_context = {
            'request': request,
        }
        serializer = PlayerSerializer(youngest_player, context=serializer_context, many=False)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='stats/oldest-player', url_name='oldest_player')
    def get_oldest_player(self, request):
        oldest_player = get_oldest_player()
        serializer_context = {
            'request': request,
        }
        serializer = PlayerSerializer(oldest_player, context=serializer_context, many=False)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='substitutes', url_name='substitutes')
    def get_substitutes(self, request):
        substitutes = get_substitute_players()
        serializer_context = {
            'request': request,
        }
        serializer = PlayerSerializer(substitutes, context=serializer_context, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='substitutes/stats/total-count', url_name='substitutes_total_count')
    def get_substitutes_count(self, request):
        substitutes_count = get_substitute_players_count()
        return Response(substitutes_count)

    @action(methods=['get'], detail=False, url_path='substitutes/stats/average-per-team', url_name='average_per_team')
    def get_average_substitutes_per_team(self, request):
        average_per_team = average_substitutes_per_team()
        return Response(average_per_team)

    @action(methods=['get'], detail=False, url_path='stats/average-per-team', url_name='average_per_team')
    def get_average_players_per_team(self, request):
        average_per_team = average_players_per_team()
        return Response(average_per_team)

    @action(methods=['get'], detail=False, url_path='stats/average-age', url_name='average_age')
    def average_players_age(self, request):
        average_age = average_players_age()
        return Response(average_age)
