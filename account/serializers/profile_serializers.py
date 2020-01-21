from rest_framework import serializers
from ..models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'user',
            'avatar',
            'biography',
            'date_of_birth',
            'gender',
            'longitude',
            'latitude',
            'address',
            'postal_code',
            'created_at'
        ]

    def get_user (self, obj):
        return {
            'first_name': obj.user.first_name or None,
            'last_name': obj.user.last_name or None,
            'email': obj.user.username,
        }
