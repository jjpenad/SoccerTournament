from rest_framework import serializers
from SoccerTournamentApp.models import  Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    #team = serializers.HyperlinkedRelatedField(many=False, view_name='team-detail', read_only=True)
    class Meta:
        model = Player
        fields = ['photo', 'firstName', 'lastName','birthDate', 'position', 'shirtNumber','firstEleven', 'team']