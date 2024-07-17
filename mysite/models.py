from django.db import models
from django.utils.text import slugify
import re

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)  # 使用 SlugField 來自動生成網址友好的 slug
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title
    def custom_slugify(value):
    # 將所有非字母、數字或橫槓的字符替換為空格
    value = re.sub(r'[^\w\s-]', '', value)
    # 將多個連續空格替換為單個橫槓
    value = re.sub(r'\s+', '-', value)
    # 使用 Django 的 slugify 函數生成 slug
    return slugify(value)
def save(self, *args, **kwargs):
        # 在保存前生成唯一的 slug
        self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)

