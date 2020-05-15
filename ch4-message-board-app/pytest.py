from django.test import TestCase
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

import pytest

from .models import Post


@pytest.mark.second
@pytest.mark.usefixtures("db", "client")
class TestHomePageView:
    def test_view_user_exists_at_proper_location(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_view_url_by_name(self, client):
        response = client.get(reverse("home"))
        assert response.status_code == 200

    def test_view_uses_correct_template(self, client):
        response = client.get(reverse("home"))
        assert response.status_code == 200
        assertTemplateUsed(response, "home.html")


@pytest.mark.third
def test_text_content(db):
    Post.objects.create(text="just a test")
    post = Post.objects.get(id=1)
    expect_object_name = f"{post.text}"
    assert expect_object_name == "just a test"
