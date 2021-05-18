from django.urls import path
from .views import *


urlpatterns = [
    path('category/',CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/',CategoryRetriveUpdateDestroyAPIView.as_view()),
    path('task/',TaskListCreateAPIView.as_view()),
    path('task/<int:pk>/',TaskRetriveUpdateDestroyAPIView.as_view())
]