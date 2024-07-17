from django.contrib import admin
from mysite.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')  # 確保這些字段在 Post 模型中是存在的

admin.site.register(Post, PostAdmin)
