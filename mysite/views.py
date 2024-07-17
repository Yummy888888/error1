from django.shortcuts import render
from datetime import datetime
from mysite.models import Post

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", {'posts': posts, 'now': now})

def post_detail(request, slug):
    # 假設你的 Post 模型有 slug 字段，根據 slug 查詢相應的文章
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        # 如果文章不存在，可以返回一個 404 錯誤頁面或其他處理方式
        from django.http import Http404
        raise Http404("Post does not exist")

    return render(request, "post_detail.html", {'post': post})
