from django.shortcuts import get_object_or_404, render
from mysite.models import Post

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})
