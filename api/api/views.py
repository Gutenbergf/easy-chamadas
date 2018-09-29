from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer, FaultSerializer
from .models import Student, Fault

# Create your views here.

class StudentViewAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class FaultViewAPI(generics.ListCreateAPIView):
    #somente usuarios com o token podem acessar
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    #permission_classes = (IsAuthenticated,)
    queryset = Fault.objects.all()
    serializer_class = FaultSerializer

class StudentSearchViewAPI(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Student.objects.filter(id_subscription=id)