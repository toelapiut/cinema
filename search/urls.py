from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets.movie import MovieDocumentView

router = DefaultRouter()
books = router.register(r'movies',
                        MovieDocumentView,
                        basename='movie_document')

urlpatterns = [
    path('', include(router.urls)),
]