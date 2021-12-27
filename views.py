from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import SessionAuthentication
# Create your views here.
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets


class TaskModelViewsSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset