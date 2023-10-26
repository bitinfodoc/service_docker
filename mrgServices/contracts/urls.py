from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'conracts/vdgo/upload', views.ContractsVdgoUpload, basename='contracts_vdgo_upload')
router.register(r'conracts/vdgo/update', views.ContractsVdgoView, basename='contracts_vdgo')

urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
]