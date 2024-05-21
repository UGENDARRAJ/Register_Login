# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    Confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'name', 'phone_number', 'password', 'Confirm_password')

    def validate(self, data):
        if data['password'] != data['Confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('Confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    # email = serializers.CharField()
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    # is_verified = serializers.BooleanField(read_only=True)

    # def validate(self, data):
    #     phone_number = data.get('phone_number')
    #     password = data.get('password')

    #     if phone_number and password:
    #         user = authenticate(username=phone_number, password=password)
    #         if user:
    #             data['is_verified'] = user.is_active  # Assuming is_active means verified
    #         else:
    #             raise serializers.ValidationError("Unable to log in with provided credentials.")
    #     else:
    #         raise serializers.ValidationError("Must include 'phone_number' and 'password'.")

    #     return data