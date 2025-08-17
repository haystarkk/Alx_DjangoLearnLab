from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blog/base.html', context)
