from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'clientEvent', ClientEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls