from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from watch.models.movie import Movie

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1,
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@INDEX.doc_type
class MovieDocument(Document):
    """
    imdb_id
    title
    summary
    release_date
    rating
    runtime
    genre
    created_at
    updated_at
    """
    id = fields.IntegerField(attr='id')
    imdb_id = fields.TextField(
        analyzer=html_strip,
        fielddata=True,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    title = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    summary = fields.TextField(
        analyzer=html_strip,
        fielddata=True,
        fields={
            'raw': fields.TextField(analyzer='keyword')
        }
    )
    release_date = fields.DateField()
    rating = fields.TextField(
        analyzer=html_strip,
        fielddata=True,
        fields={
            'raw': fields.TextField(analyzer='keyword')
        }
    )
    runtime = fields.TextField(
        analyzer=html_strip,
        fielddata=True,
        fields={
            'raw': fields.TextField(analyzer='keyword')
        }
    )
    genre = fields.TextField(
        attr='genre_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', multi=True),
            'suggest': fields.CompletionField(multi=True),
        },
        multi=True
    )
    created_at = fields.DateField()

    class Django(object):
        """
        The model associate with this Document
        """
        model = Movie
