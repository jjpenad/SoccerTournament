from rest_framework import viewsets
from rest_framework.decorators import action
from SoccerTournamentApp.logic.TechnicalStaff import *
from SoccerTournamentApp.models import TechnicalStaff
from ..Serializers import TechnicalStaffSerializer
from rest_framework.response import Response

class TechnicalStaffViewSet(viewsets.ModelViewSet):
    queryset = TechnicalStaff.objects.all()
    serializer_class = TechnicalStaffSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        staff = get_technicalStaff()
        serializer_context = {
            'request': request,
        }
        serializer = TechnicalStaffSerializer(staff, context=serializer_context, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='stats/oldest-technical-staff', url_name='oldest_technical_staff')
    def get_oldest_technical_staff(self, request):
        oldest_technical_staff = get_oldest_tecnicalStaff()
        serializer_context = {
            'request': request,
        }
        serializer = TechnicalStaffSerializer(oldest_technical_staff, context=serializer_context, many=False)
        return Response(serializer.data)