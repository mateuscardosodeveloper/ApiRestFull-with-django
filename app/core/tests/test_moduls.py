from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_created_user(self):
        """Test when created user if have email"""
        email = "mateus@email.com"
        password = "123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_low_case_email(self):
        """Test when create a user check email is normalized"""
        email = 'mateus@EMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """Test when create the superuser"""
        user = get_user_model().objects.create_superuser(
            'mateus@email.com',
            'mateus'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
