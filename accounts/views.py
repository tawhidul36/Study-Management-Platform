from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ForgotPasswordSerializer,
    VerifyOTPSerializer,
    ResetPasswordSerializer
)
from .models import CustomUser
from .utils import generate_otp, send_otp_email


class RegisterView(APIView):
    """
    POST: Register a new user
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)

            return Response({
                "success": True,
                "message": "User registered successfully",
                "data": {
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    },
                    "tokens": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                }
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    POST: Login user and return JWT tokens
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]

            user.last_login_time = timezone.now()
            user.save(update_fields=["last_login_time"])

            refresh = RefreshToken.for_user(user)

            return Response({
                "success": True,
                "message": "Login successful",
                "data": {
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    },
                    "tokens": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                }
            }, status=status.HTTP_200_OK)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(APIView):
    """
    POST: Send OTP to user's email
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]

            try:
                user = CustomUser.objects.get(email=email)

                otp = generate_otp()
                user.otp = otp
                user.otp_created_at = timezone.now()
                user.save(update_fields=["otp", "otp_created_at"])

                if send_otp_email(email, otp):
                    return Response({
                        "success": True,
                        "message": "OTP sent successfully",
                        "data": {"email": email}
                        
                    }, status=status.HTTP_200_OK)

                return Response({
                    "otp": otp,
                    "success": False,
                    "message": "Failed to send OTP"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            except CustomUser.DoesNotExist:
                return Response({
                    "success": False,
                    "message": "No user found with this email"
                }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    """
    POST: Verify OTP
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]

            return Response({
                "success": True,
                "message": "OTP verified successfully",
                "data": {"email": user.email}
            }, status=status.HTTP_200_OK)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    """
    POST: Reset password using OTP
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            new_password = serializer.validated_data["new_password"]

            user.set_password(new_password)
            user.otp = None
            user.otp_created_at = None
            user.save()

            return Response({
                "success": True,
                "message": "Password reset successfully",
                "data": {"email": user.email}
            }, status=status.HTTP_200_OK)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
