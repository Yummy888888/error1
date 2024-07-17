from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # 假設這裡是你的 SlugField

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # 使用標題來生成 slug
        super().save(*args, **kwargs)
