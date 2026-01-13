from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                "confirm_password": "Passwords do not match."
            })
        return attrs

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return CustomUser.objects.create_user(**validated_data)



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError({
                "detail": "Invalid email or password."
            })

        if not user.is_active:
            raise serializers.ValidationError({
                "detail": "User account is disabled."
            })

        attrs['user'] = user
        return attrs


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("User not found.")
        return value



class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(min_length=6, max_length=6)

    def validate(self, attrs):
        try:
            user = CustomUser.objects.get(email=attrs['email'])
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({"email": "Invalid email."})

        if not user.otp:
            raise serializers.ValidationError({"otp": "OTP not found."})

        if user.otp != attrs['otp']:
            raise serializers.ValidationError({"otp": "Invalid OTP."})

        if not user.is_otp_valid():
            raise serializers.ValidationError({"otp": "OTP expired."})

        attrs['user'] = user
        return attrs


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(min_length=6, max_length=6)
    new_password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                "confirm_password": "Passwords do not match."
            })

        try:
            user = CustomUser.objects.get(email=attrs['email'])
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({"email": "Invalid email."})

        if user.otp != attrs['otp']:
            raise serializers.ValidationError({"otp": "Invalid OTP."})

        if not user.is_otp_valid():
            raise serializers.ValidationError({"otp": "OTP expired."})

        attrs['user'] = user
        return attrs
