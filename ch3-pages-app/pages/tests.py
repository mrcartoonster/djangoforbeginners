import pytest
from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


@pytest.mark.first
@pytest.mark.usefixtures('client')
class TestSimple:
    def test_home_page_status_code(self, client):
        resp = client.get('/')
        assert resp.status_code == 200

    def test_about_page_status_code(self, client):
        resp = client.get('/about/')
        assert resp.status_code == 200
