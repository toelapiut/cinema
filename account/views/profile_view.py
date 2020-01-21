from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.profile import Profile
from ..serializers.profile_serializers import ProfileSerializer
from rest_framework import status


class ProfileView(APIView):
    """
    GET current user profile information
    NOTE: User needs to be authenticated
    """
    def get(self, request, format=None):
        user_profile = Profile.objects.get(user__id=request.user.id)
        serializer = ProfileSerializer(user_profile)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
