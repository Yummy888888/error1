from django.shortcuts import get_object_or_404, render
from mysite.models import Post
from datetime import datetime

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", {'posts': posts, 'now': now})
