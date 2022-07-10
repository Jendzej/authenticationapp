from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
import random
from django.db import IntegrityError


class ModelPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    post_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.TextField()

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # if not self.slug:
        #     self.slug = slugify(self.title)
        # super(ModelPost, self).save(*args, **kwargs)
        try:
            self.slug = ''.join(str(random.randint(0, 9)) for _ in range(8))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title


class Comment(models.Model):
    name = models.TextField()
    content = models.TextField()
    post = models.ForeignKey(ModelPost, on_delete=models.CASCADE, related_name="comments")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.content
