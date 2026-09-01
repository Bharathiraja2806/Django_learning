from django.db import models
from django.utils.text import slugify


class Categories(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE, related_name='posts')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
