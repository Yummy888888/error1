from django.shortcuts import render
from datetime import datetime
from mysite.models import Post
def homepage(request):
  posts=Post.objects.all()
  now=datetime.now()
  return render(request,"index.html",locals())
