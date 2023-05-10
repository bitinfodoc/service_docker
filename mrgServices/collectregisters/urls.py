from django.urls import include, path
from rest_framework import routers
from collectregisters import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'registers/site-readings', views.getReadings, basename='get_readings_site')

urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
]