from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)  # 使用 SlugField 來自動生成網址友好的 slug
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title
