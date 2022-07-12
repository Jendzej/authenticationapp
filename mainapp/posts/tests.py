from django.test import TestCase
from .models import Comment, ModelPost


class PostsTestCase(TestCase):
    def setUp(self):
        ModelPost.objects.create(post_content='test', title='test', user='usertest')


class CommentsTestCase(TestCase):
    def setUp(self):
        Comment.objects.create(content='test', user='usertest')
