from django.urls import path

from post import views

urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view()),
    path('posts/search/title/', views.PostTitleSearchAPIView.as_view()),
    path('posts/search/tag/', views.PostTagSearchAPIView.as_view()),
    path('post/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view()),
]
