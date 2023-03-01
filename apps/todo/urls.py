from django.urls import path
from rest_framework.routers  import DefaultRouter

from .views import ToDoAPI,ToDoAllDestroyAPIView

router = DefaultRouter()
router.register("todo", ToDoAPI, basename="users")


urlpatterns = [
    path('api/todo/destroy/all/', ToDoAllDestroyAPIView.as_view(), name = "todo_all_destroy")
]
urlpatterns+=router.urls