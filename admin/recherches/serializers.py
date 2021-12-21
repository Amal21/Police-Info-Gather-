#from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers
from .models import Recherche


class RechercheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recherche
        fields = '__all__'

#class ProductDocumentSerializer(DocumentSerializer):
    #class Meta:
        #document = ProductDocument
        #fields = [
            #'title',
            #'image'

        #]

