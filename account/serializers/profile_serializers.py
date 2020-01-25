from rest_framework import serializers
from ..models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'user',
            'avatar',
        ]

    def get_user (self, obj):
        return {
            'first_name': obj.user.first_name or None,
            'last_name': obj.user.last_name or None,
            'email': obj.user.username,
            'date_of_birth': obj.date_of_birth,
            'gender': obj.gender,
            'bio': obj.biography,
            'location': {
                'long': obj.longitude,
                'lat': obj.latitude,
                'address': obj.address,
                'postal_code': obj.postal_code,
            },
            'created_at': obj.created_at
        }
