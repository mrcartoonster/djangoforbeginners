import pytest

from .models import Post


@pytest.fixture()
def user(db, django_user_model):
    """Fixture for a customer user model fixture to pass to test."""
    the_user = django_user_model.objects.create(
        username="testuser", email="test@email.com", password="secret"
    )
    return the_user


@pytest.fixture()
def post(user):
    """Fixture of a sample post to test model against."""
    the_post = Post.objects.create(
        title="A good title", body="Nice body content", author=user
    )
    return the_post
