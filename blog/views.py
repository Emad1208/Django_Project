from django.shortcuts import render

def index_blog_view(request):
    return render(request, 'blogs/blog-home.html')


def single_blog_view(request):
    return render(request, 'blogs/blog-single.html')