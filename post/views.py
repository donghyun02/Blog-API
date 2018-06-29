from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

class PostTitleSearchAPIView(APIView):
    def get(self, request):
        title = request.GET.get('keyword', '')
        posts = Post.objects.filter(title__contains=title).order_by('-created_at')
        serialized_posts = PostSerializer(posts, many=True)

        return Response(serialized_posts.data)

class PostTagSearchAPIView(APIView):
    def get(self, request):
        tag_name = request.GET.get('keyword', '')
        posts = Post.objects.filter(tags__name__exact=tag_name).order_by('-created_at')
        serialized_posts = PostSerializer(posts, many=True)

        return Response(serialized_posts.data)
