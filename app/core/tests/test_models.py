from django.test import TestCase
from django.contrib.auth import get_user_model

from .. import models


def sample_user(email='admin@mail.com', password='Admin123'):
    """
    Create a sample user
    :param email:
    :param password:
    :return:
    """

    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with email is successful
        :return:
        """
        email = "test@mail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test that email for a new user is normalized
        :return:
        """

        email = "test@MAIL.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating user with no email raises error
        :return:
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """
        Test creating a new superuser
        :return:
        """

        user = get_user_model().objects.create_superuser(
            'test@mail.com', 'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """
        Test the tag string representation
        :return:
        """

        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
