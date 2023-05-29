from django.urls import include, path
from rest_framework import routers
from collectregisters import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'registers/site-readings', views.getReadings, basename='get_readings_site')
router.register(r'registers/site-contacts', views.getContacts, basename='get_contacts_site')

urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
]