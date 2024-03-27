from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer
from .models import User


class UserView(APIView):
    '''
    Для админов, чтобы просматривать пользователей, которые вообще есть
    '''

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({'users': serializer.data})
