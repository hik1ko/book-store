from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField

from apps.account.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = CharField(write_only=True)
    password2 = CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", 'email', "password", "password2")


    def create(self, validated_data):
        account = User.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )
        account.set_password(validated_data["password"])
        account.save()
        return account

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError(detail="Passwords must be match", code="password")

        return attrs
