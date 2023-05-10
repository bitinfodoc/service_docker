from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'rng-base', views.RngBase, basename='rng_base')

urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
]