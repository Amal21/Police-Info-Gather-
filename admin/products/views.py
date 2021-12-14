from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters

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



from .models import Product, User
from .serializers import ProductSerializer#ProductDocumentSerializer
#from .documents import ProductDocument




from .producer import publish
from .serializers import ProductSerializer
import random

#class ProductSearchWithESViewSet(DocumentViewSet):

    #document = ProductDocument
    #serializer_class = ProductDocumentSerializer
    #filter_backends = [SearchFilterBackend]
    #search_fields = [
        #'title',

    #]
    #filter_fields= {
        #'title' : 'title',
        #'image' : 'image',

    #}






class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    def search(self, request):

        queryset = Product.objects.all()
        #print(queryset)

        title = self.request.query_params.get('title')
        #print(title)

        queryset = queryset.filter(title=title)
        #print(queryset)

        serializer = ProductSerializer(queryset, many=True)

        return  Response(serializer.data)



    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    #def retrieve(self, request, pk=None):
        #product = Product.objects.get(title=pk)
        #serializer = ProductSerializer(product)
        #return Response(serializer.data)


    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)




class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })

