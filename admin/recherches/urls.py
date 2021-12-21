from django.urls import path
from .views import RechercheViewSet, UserAPIView

urlpatterns = [


    path('recherches/find', RechercheViewSet.as_view({
        'get': 'search',

    })),


    path('recherches', RechercheViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    
    path('recherches/<str:pk>', RechercheViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view())

]
