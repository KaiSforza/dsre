from django.test import TestCase
from django.test import Client


class TestIndexView(TestCase):
    def test_get_no_header(self):
        c = Client()
        r = c.get('/')
        self.assertEqual(r.content, b'<p>Hello, World</p>')

    def test_get_header(self):
        c = Client()
        r = c.get('/', HTTP_ACCEPT='application/json')
        self.assertEqual(r.content, b'{"message": "Good morning"}')
