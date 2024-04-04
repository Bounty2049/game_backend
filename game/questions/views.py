from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response


from .serializers import QuestionSerializer, QuestionUsedSerializer
from .models import Question, QuestionUsed


class QuestionViewSet(generics.ListCreateAPIView):
    '''
    Простотр и создание новых вопросов
    '''
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]


    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionSerializer(queryset, many=True)

        return Response(serializer.data)
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    


class QuesetionRetrieve(generics.RetrieveAPIView):
    '''Получить данные конкретного вопроса по id'''
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class QuestionUsedView(generics.ListCreateAPIView):
    '''
    Дает возможность фронту считывать те вопросы которые уже были, 
    а так же их количество. 
    Примечание:
        данная реализация позволяет сыграть в игру только 3 раза, поскольку потом
        БД переполняется и фронт делая запрос падает в бесконечный цикл
    '''
    queryset = QuestionUsed.objects.all()
    serializer_class = QuestionUsedSerializer
    permission_classes = [AllowAny]
    

    def list(self, request):
        queryset = QuestionUsed.objects.all()
        serializer = QuestionUsedSerializer(queryset, many=True)

        return Response(serializer.data)
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)        