from django.test import TestCase

from github_oauth.custom_user.models import CustomUser


class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create(username="test_user", password="testing123")
        user.full_clean()  # this will fail if required fields are not provided
