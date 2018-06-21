from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from post.models import Post
from post.serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer