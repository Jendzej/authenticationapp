from django.test import SimpleTestCase
from django.urls import resolve, reverse
from posts.views import posts_page, adding_post, edit_post, delete_post, get_pdf
from accounts.views import SignUpView
from django.views.generic.base import TemplateView


class TestUrls(SimpleTestCase):
    """Urls tests"""
    def test_posts_resolve(self):
        url = reverse('posts')
        print(f'1 :    {resolve(url)}')
        self.assertEquals(resolve(url).func, posts_page)

    def test_add_resolve(self):
        url = reverse('add')
        print(f'2 :    {resolve(url)}')
        self.assertEquals(resolve(url).func, adding_post)

    def test_edit_resolve(self):
        url = reverse('edit', args=['1'])
        print(f'3 :    {resolve(url)}')
        self.assertEquals(resolve(url).func, edit_post)

    def test_delete_resolve(self):
        url = reverse('delete', args=['1'])
        print(f'4 :    {resolve(url)}')
        self.assertEquals(resolve(url).func, delete_post)

    def test_pdf_resolve(self):
        url = reverse('get_pdf', args=['1'])
        print(f'5 :    {resolve(url)}')
        self.assertEquals(resolve(url).func, get_pdf)

    def test_home_resolve(self):
        url = reverse('home')
        print(f'6 :    {resolve(url)}')
        self.assertEquals(resolve(url).func.view_class, TemplateView)

    def test_signup_resolve(self):
        url = reverse('signup')
        print(f'7 :    {resolve(url)}')
        self.assertEquals(resolve(url).func.view_class, SignUpView)
