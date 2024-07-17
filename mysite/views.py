from django.views.generic import DetailView
from django.shortcuts import render
from datetime import datetime
from mysite.models import Post

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", {'posts': posts, 'now': now})
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
