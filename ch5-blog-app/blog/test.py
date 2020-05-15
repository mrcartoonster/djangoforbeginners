import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains, assertTemplateUsed

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
def test_post_list_view(client, post):
    """Converting list view to pytest."""
    response = client.get(reverse("home"))
    assert response.status_code == 200
    assertContains(response, "Nice body content")
    assertTemplateUsed(response, "home.html")
    # Crude way of doing it.
    assert str.encode("Nice body content") in response.content


@pytest.mark.fourth
def test_post_detail_view(client, post):
    """Convertin detail view to pytest."""
    response = client.get('/post/1/')
    no_response = client.get('/post/11111/')
    assert response.status_code == 200
    assert no_response.status_code == 404
    assertContains(response, "A good title")
    assertTemplateUsed(response, "post_detail.html")
