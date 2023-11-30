from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class CreateStudentList(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class RetrieveStudentList(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class UpdateStudentList(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class DestroyStudata(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class ListCreateStudata(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class RetrieveUpdateStudata(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class RetrieveDestroyStudata(RetrieveDestroyAPIView):
    queryset =Student.objects.all()
    serializer_class=StudentSerializer

class RetrieveUpdateDelStudata(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer