from django.urls import path
from .views import BlogsList, BlogsDetail

urlpatterns = [
    path('', BlogsList.as_view(), name='Blogs_list'),
    path('<int:pk>/', BlogsDetail.as_view(), name='Blogs_detail'),
]