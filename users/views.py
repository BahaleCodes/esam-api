from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, filters, generics, permissions
from .models import *

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:

                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Profile_list(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.filter(role='artist')

class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    def get_queryset(self, user):
        queryset = Profile.objects.get(user=user)
        return queryset


    def get(self, request, format=None):
        user = request.user
        profile = self.get_queryset(user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    