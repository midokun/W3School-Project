import unittest
from django.urls import path, include
from . import views

class TestURLs(unittest.TestCase):

    def test_blank_urls(self):
        url = path('', include('blank.urls'))
        self.assertEqual(url.pattern.regex.pattern, '^$')
        self.assertEqual(url.callback, include('blank.urls'))

    def test_index_url(self):
        url = path('', views.index, name='index')
        self.assertEqual(url.pattern.regex.pattern, '^$')
        self.assertEqual(url.callback, views.index)
        self.assertEqual(url.name, 'index')

if __name__ == '__main__':
    unittest.main()