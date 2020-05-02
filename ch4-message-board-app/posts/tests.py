import pytest
from django.test import TestCase
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')

class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


@pytest.mark.second
def test_text_content(db):
    Post.objects.create(text="just a test")
    post = Post.objects.get(id=1)
    expected_object_name = f"{post.text}"
    assert expected_object_name == "just a test"


@pytest.mark.third
@pytest.mark.usefixtures("db", "client")
class TestHomePageView:
    def setUp(self, db):
        Post.objects.create(text="this is another test")

    def test_view_user_exists_at_proper_location(self, client):
        resp = client.get("/")
        assert resp.status_code == 200

    def test_view_url_by_name(self, client):
        resp = client.get(reverse("home"))
        assert resp.status_code == 200

    def test_view_uses_correct_template(self, client):
        resp = client.get(reverse("home"))
        assert resp.status_code == 200
        assertTemplateUsed(resp, "home.html")
