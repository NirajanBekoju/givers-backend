from customuser.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        # fields = ['id', 'username', 'email', ]
        exclude = ('password', 'otp', 'activation_key')

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.full_name
        if name == '':
            name = obj.email
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'username', 'email',
                  'volunteer', 'organization', 'token', 'images', 'active', 'staff', 'verify', 'reject', ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)
