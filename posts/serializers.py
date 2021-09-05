from rest_framework import serializers
from .models import Blog

class BLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','user','card','author')