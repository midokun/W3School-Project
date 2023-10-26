import unittest
from django.urls import resolve
from django.test import SimpleTestCase

class TestURLs(SimpleTestCase):

    def test_blank_url_resolves(self):
        url = resolve('/')
        self.assertEqual(url.namespace, 'blank')

    def test_admin_url_resolves(self):
        url = resolve('/admin/')
        self.assertEqual(url.namespace, 'admin')

    def test_app_url_resolves(self):
        url = resolve('/your_app/')
        self.assertEqual(url.namespace, 'your_app')

    def test_invalid_url_resolves(self):
        url = resolve('/invalid_url/')
        self.assertNotEqual(url.namespace, 'your_app')

    def test_wildcard_url_resolves(self):
        url = resolve('/subdomain.midocyberguard.com/')
        self.assertEqual(url.namespace, 'your_app')

if __name__ == '__main__':
    unittest.main()
