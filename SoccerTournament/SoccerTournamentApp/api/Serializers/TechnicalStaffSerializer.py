from rest_framework import serializers
from SoccerTournamentApp.models import TechnicalStaff

class TechnicalStaffSerializer(serializers.HyperlinkedModelSerializer):
    #team = serializers.HyperlinkedRelatedField(many=False, view_name='team-detail', read_only=True)
    class Meta:
        model = TechnicalStaff
        fields = ['firstName', 'lastName', 'birthDate', 'nationality', 'rol', 'team']