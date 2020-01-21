from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import profile_view

urlpatterns = [
    path('profile',  profile_view.ProfileView.as_view(), name="user_profile")
]
