from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'ls/upload', views.LsUpload, basename='rng_ls_upload')
router.register(r'ls/validate', views.LsValidate, basename='rng_ls_validate')

urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
]