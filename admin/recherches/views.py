from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

#from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
#from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)



from .models import Recherche, User
from .serializers import RechercheSerializer#ProductDocumentSerializer
#from .documents import ProductDocument




from .producer import publish
from .serializers import RechercheSerializer
import random

#class ProductSearchWithESViewSet(DocumentViewSet):

    #document = ProductDocument
    #serializer_class = ProductDocumentSerializer
    #filter_backends = [SearchFilterBackend]
    #search_fields = [
        #'title',
        #'image'
    #]
    #filter_fields= {
        #'title' : 'title',
    #}






class RechercheViewSet(viewsets.ViewSet):

    def list(self, request):
        recherches = Recherche.objects.all()
        serializer = RechercheSerializer(recherches, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RechercheSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('recherche_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



    def search(self, request):

        queryset = Recherche.objects.all()
        #print(queryset)

        cin = self.request.query_params.get('cin')
        #print(title)

        queryset = queryset.filter(cin=cin)
        #print(queryset)

        serializer = RechercheSerializer(queryset, many=True)

        return  Response(serializer.data)
        

    def retrieve(self, request, pk=None):
        recherche = Recherche.objects.get(id=pk)
        serializer = RechercheSerializer(recherche)
        return Response(serializer.data)

    def update(self, request, pk=None):
        recherche = Recherche.objects.get(id=pk)
        serializer = RechercheSerializer(instance=recherche, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('recherche_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        recherche = Recherche.objects.get(id=pk)
        recherche.delete()
        publish('recherche_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)




class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })

