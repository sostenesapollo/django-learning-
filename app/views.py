from app.models import Todo

from app.serializers import TodoSerializer

from rest_framework import generics, viewsets

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer