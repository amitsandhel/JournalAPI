from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', views.JMIRViewSet)


urlpatterns = [
    path('crossref', views.JMIRCrossRef.as_view(), name='crossref'),
    path('ncbi', views.ncbi, name='ncbi'),
    path('aboutus', views.AboutView.as_view(), name='aboutus'),
    #DRF urls
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]#urls of app 
