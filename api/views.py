from django.shortcuts import render
from rest_framework import generics,  status
from rest_framework.response import Response 
from .models import BlogPost
from .serializers import BlogPostsSerializer
from rest_framework.views import APIView


# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostsSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostsSerializer
    lookup_field = 'id'

class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get('title', None)

        if title is not None:
            posts = BlogPost.objects.filter(title__icontains=title)
        else:
            posts = BlogPost.objects.all()

        serializer = BlogPostsSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)