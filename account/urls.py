from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import profile_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('profile', profile_view.ProfileView.as_view(), name="user_profile")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
