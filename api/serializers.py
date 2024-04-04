# To convert python objest to JSON

from rest_framework import serializers
from .models import BlogPost

class BlogPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'