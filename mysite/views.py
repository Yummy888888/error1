from django.views.generic import DetailView
from mysite.models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()  # 這裡可以自定義需要的 queryset 條件
    slug_field = 'slug'  # 如果使用 slug 來查找，確保與模型中的字段名稱一致
    slug_url_kwarg = 'slug'  # URLconf 中的參數名稱
