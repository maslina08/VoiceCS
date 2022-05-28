from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import FiltredPhonesViewSet

router = routers.DefaultRouter()
router.register('phones', FiltredPhonesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
