from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog
from .serializers import BLogSerializer

class BlogsList(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BLogSerializer

class BlogsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BLogSerializer