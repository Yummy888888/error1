from django.db import models
from django.utils.text import slugify
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)  # 使用 SlugField 來自動生成網址友好的 slug
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        # 在保存前自動生成slug
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
