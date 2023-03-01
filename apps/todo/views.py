from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
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
    