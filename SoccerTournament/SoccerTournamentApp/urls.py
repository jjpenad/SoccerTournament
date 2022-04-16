from rest_framework import routers
from django.urls import include, path
from .api.Viewsets import TeamViewSet, PlayerViewSet, TechnicalStaffViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'teams', TeamViewSet) 
router.register(r'technicalStaff', TechnicalStaffViewSet)

urlpatterns = [
    path("", include(router.urls)),
]