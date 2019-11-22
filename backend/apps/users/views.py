from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User

from .models import UserProfile

from .serializers import UserSerializer

from . import services


class UserRegisterView(APIView):
    permission_classes = []
    authentication_classes = []

    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        email = serializers.EmailField()
        password = serializers.CharField()
        user_type = serializers.CharField()
        full_name = serializers.CharField()
        phone_number = serializers.CharField()
        address = serializers.CharField()
        buyer_type = serializers.CharField()

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = create_user(**serializer.validated_data)

        return Response()


class UserProfileDetailView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class SellerListView(APIView):
    def get(self, request, *args, **kwargs):
        profiles = UserProfile.objects.filter(user_type='seller')
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serilizer.data)
