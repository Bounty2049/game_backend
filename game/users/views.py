from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer
from .models import User


class UserView(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({'users': serializer.data})


    # def post(self, request):
    #     username = request.data.get('username')
    #     email = request.data.get('password')
    #     phone = request.data.get('phone_number')


@api_view(['POST'])
def registration(request):
    username = request.data.get('username')
    email = request.data.get('email')
    phone = request.data.get('phone')
    password = request.data.get('password')

    if username is None or password is None or email is None or phone is None:
        return Response({'error': 'all area required'})
    
    user = authenticate(request._request, username=username, password=password)

    try:
        user = User.objects.create_user(username=username, password=password, email=email, phone=phone)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    
    refresh_token = RefreshToken.for_user(user)

    response_data = {
        'refresh_token': str(refresh_token),
        'access_token': str(refresh_token.access_token)
    }

    response = Response(response_data)

    return response

