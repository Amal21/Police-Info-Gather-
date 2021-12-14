#from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers
from .models import Product
#from .documents import ProductDocument

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

#class ProductDocumentSerializer(DocumentSerializer):
    #class Meta:
        #document = ProductDocument
        #fields = [
            #'title',
            #'image'

        #]

