import pytest

from users.models import User


@pytest.mark.django_db
class TestUserModel:

    def test_soft_delete(self):
        user = User.objects.create(username="Test")
        assert user.is_deleted == False
        user.soft_delete()
        assert user.is_deleted == True

    def test_user_str(self):
        user = User.objects.create(
            username="Test", first_name="Adam", last_name="Parker"
        )
        assert str(user) == "Adam Parker"
