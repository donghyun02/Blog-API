from django.urls import path

from post import views

urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view()),
]