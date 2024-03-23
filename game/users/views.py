from rest_framework.views import APIView
from rest_framework.response import Response

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

