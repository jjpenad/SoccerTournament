from rest_framework import serializers
from SoccerTournamentApp.models import Team

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="team-detail")
    class Meta:
        model = Team
        fields = ['url','id','name', 'flagImage', 'teamCrest'] 