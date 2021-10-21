from django.core.exceptions import ValidationError
from django.test import TestCase, Client, LiveServerTestCase

from github_oauth.custom_user.models import CustomUser


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username="test_user", password="testing123"
        )

    def test_create_user(self):
        self.user.full_clean()  # this will fail if required fields are not provided

    def test_model_validation(self):
        self.user.email = "invalid.email.address"
        with self.assertRaises(ValidationError):
            self.user.full_clean()


class UpdateFormTestCase(LiveServerTestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username="test_user", password="testing123"
        )

    def test_can_update_profile(self):
        self.assertEqual("", self.user.email)
        c = Client()
        c.force_login(self.user)
        c.post("/myprofile/", {"first_name": "test", "email": "test@example.com"})
        self.user.refresh_from_db()
        self.assertEqual("test@example.com", self.user.email)
        self.assertEqual("test", self.user.first_name)
        self.assertEqual("", self.user.last_name)
        self.assertEqual(
            "test_user", self.user.username
        )  # username should not have changed even though it was not POSTed
