from django_elasticsearch_dsl import (
    Document ,
    fields,

)
from django_elasticsearch_dsl.registries import registry
from .models import Recherche

@registry.register_document
#@PUBLISHER_INDEX.doc_type
class RechercheDocument(Document):

    class Index:
        name = 'recherches'
        settings={'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:

        model= Recherche
        fields ={
            'cin',
            'description',
        }

