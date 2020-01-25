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
    filter=["standard", "lowercase", "stop", "snowball"],
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
    imdb_id = fields.IntegerField(attr='id')
    title = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )
    summary = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword')
        }
    )
    release_date = fields.DateField()
    rating = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword')
        }
    )
    runtime = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword')
        }
    )
    genre = fiels.StringField(
        attr='genre_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword', multi=True),
            'suggest': fields.CompletionField(multi=True),
        },
        multi=True
    )
    created_at = fields.DateField()

    class Django(object):
        """
        Inner nested class Django.
        The model associate with this Document
        """
        model = Movie
