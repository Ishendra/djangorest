from rest_framework import serializers
from .models import Roles
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Roles
        fields='__all__'

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( 'password','is_staff','first_name','username',  'last_name', 'email' )
    