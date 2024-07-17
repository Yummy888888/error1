from django.shortcuts import render
from datetime import datetime
from mysite.models import Post
def homepage(request):
  posts=Post.objects.all()
  now=datetime.now()
  return render(request,"index.html",locals())
def post_detail(request, slug):
    # 實現詳細視圖的邏輯，這裡示範了一個簡單的方式
    post = Post.objects.get(slug=slug)
    return render(request, "post_detail.html", {'post': post})
