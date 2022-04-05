from django.urls import path, include
from home.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('contact', views.ContactViewSet, basename='contact')
router.register('service', views.ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls))
]