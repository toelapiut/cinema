import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from ..documents.movie import MovieDocument


class MovieDocumentSerializer(DocumentSerializer):
    """
    Serializer for the Movie document.
    """
    class Meta(object):
        document = MovieDocument

        fields = (
            'id',
            'imdb_id',
            'title',
            'summary',
            'release_date',
            'rating',
            'runtime',
            'genre',
            'created_at',
        )
