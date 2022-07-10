"""Creating and configuration app models"""
import random
from django.db import models
from django.db import IntegrityError


class ModelPost(models.Model):
    """Post model data types configuration"""
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    post_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.TextField()

    def save(self, *args, **kwargs):
        """Post's slug configuration"""
        try:
            self.slug = ''.join(str(random.randint(0, 9)) for _ in range(8))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)

    class Meta:
        """Posts ordering"""
        ordering = ['created_on']


class Comment(models.Model):
    """Comment model data types configuration"""
    name = models.TextField()
    content = models.TextField()
    post = models.ForeignKey(ModelPost, on_delete=models.CASCADE, related_name="comments")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Post ordering"""
        ordering = ['created_on']
