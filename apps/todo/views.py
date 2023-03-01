from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import filters
from .serializers import ToDo,ToDoSerializer

# Create your views here.
class ToDoAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              mixins.UpdateModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'description')

class ToDoAllDestroyAPIView(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    def delete(self, request, *args, **kwargs):
        todo = ToDo.objects.filter()
        todo = [t for t in todo.delete()]
        return Response({'delete' : 'Все такски удалены'})