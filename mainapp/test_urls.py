from django.test import SimpleTestCase
from django.urls import resolve, reverse
from posts.views import posts_page, adding_post
from accounts.views import SignUpView
from django.views.generic.base import TemplateView


class TestUrls(SimpleTestCase):
    """Urls tests"""
    def test_posts_resolve(self):
        url = reverse('posts')
        print(resolve(url))
        self.assertEquals(resolve(url).func, posts_page)

    def test_add_resolve(self):
        url = reverse('add')
        print(resolve(url))
        self.assertEquals(resolve(url).func, adding_post)

    def test_home_resolve(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TemplateView)

    def test_signup_resolve(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, SignUpView)

