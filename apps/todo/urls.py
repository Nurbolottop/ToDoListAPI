from django.contrib import admin
from rest_framework.routers  import DefaultRouter

from .views import ToDoAPI
router = DefaultRouter()
router.register("todo", ToDoAPI, basename="users")


urlpatterns = [

]
urlpatterns+=router.urls