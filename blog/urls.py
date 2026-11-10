from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('blog', index_blog_view, name= 'index'),
    path('blog/single/', single_blog_view, name= 'single'),
]