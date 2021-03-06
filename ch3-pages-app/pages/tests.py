import pytest
from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)


@pytest.mark.first
def test_home_page_status_code(client):
    """Assure homeage is working."""

    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.second
def test_about_page_staus_code(client):
    """Assert the about page exists."""

    response = client.get("/about/")
    assert response.status_code == 200
