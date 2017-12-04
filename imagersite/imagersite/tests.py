"""Module to test view and authentication."""
from django.test import Client, TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core import mail

class ViewTests(TestCase):
    """Class to test views."""

    def setUp(self):
        """Init client to test against."""
        self.client = Client()

    def test_home_status_code_200(self):
        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)

    def test_login_status_code_200(self):
        response = self.client.get(reverse_lazy('auth_login'))
        self.assertEqual(response.status_code, 200)

    def test_registration_status_code_200(self):
        response = self.client.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_home_returns_template(self):
        response = self.client.get(reverse_lazy('home'))
        self.assertTemplateUsed(response,'imagersite/home.html')

    def test_cant_log_in_unregistered_user(self):
        response = self.client.post(
            reverse_lazy('auth_login'),
            {
                'username': 'bob',
                'password': 'bobsucks'
            })
        self.assertContains(response, bytes('Please enter a correct username and password', 'utf8'))

    def test_register_new_user(self):
        data = {
            'username': 'bob',
            'password1': 'bobstheman',
            'password2': 'bobstheman',
            'email': 'bob@bob.gov'
        }
        response = self.client.post(
            reverse_lazy('registration_register'),
            data
            )
        self.assertTrue(response.status_code, 302)
        self.assertTrue(response.url == reverse_lazy('registration_complete'))

    def test_email_sent_after_register(self):
        data = {
            'username': 'bob',
            'password1': 'bobstheman',
            'password2': 'bobstheman',
            'email': 'bob@bob.gov'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.subject, "Imagersite Activation")
        self.assertIn('bob@bob.gov', email.to)

    def test_email_link_activates_account(self):
        data = {
            'username': 'bob',
            'password1': 'bobstheman',
            'password2': 'bobstheman',
            'email': 'bob@bob.gov'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        content = mail.outbox[0].message().get_payload()
        link = content.split('\n\n')[1]
        self.client.get(link)
        self.assertTrue(User.objects.count() == 1)
        user = User.objects.get(username='bob')
        self.assertTrue(user.is_active)