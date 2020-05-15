from django.urls import reverse

import pytest

from .models import Post


@pytest.mark.django_db
def test_string_representation():
    """Rewritten test in pytest for test representation."""
    post = Post(title="A sample title")
    assert str(post) == post.title


@pytest.mark.second
def test_post_content(post):
    """Using post fixture to test content is actually available."""
    assert f"{post.title}" == "A good title"
    assert f"{post.author}" == "testuser"
    assert f"{post.body}" == "Nice body content"


@pytest.mark.third
@pytest.mark.django_db
def test_post_list_view(client):
    """Converting list view to pytest."""
    response = client.get(reverse("home"))
    assert response.status_code == 200
