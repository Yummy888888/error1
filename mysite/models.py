from django.db import models
from django.utils.text import slugify
import urllib.parse

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    original_url = models.URLField(max_length=200)  # 添加一个字段用来存储原始 URL

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # 使用标题生成 slug
        self.original_url = urllib.parse.quote(self.original_url)  # 编码原始 URL
        super().save(*args, **kwargs)
