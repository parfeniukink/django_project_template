from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as _UserCreateSerializer
from djoser.serializers import UserSerializer as _UserSerializer

User = get_user_model()


class UserCreateSerializer(_UserCreateSerializer):
    class Meta(_UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "password")


class UserSerializer(_UserSerializer):
    class Meta(_UserSerializer.Meta):
        model = User
        fields = ("id", "email", "username", "is_active", "last_login")
