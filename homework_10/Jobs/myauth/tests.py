from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.


class TestUserAuth(TestCase):
    def setUp(self) -> None:

        self.user_data = {
            'username': 'Kirill',
            'email': 'kirill@lanit.ru',
            'password': 'kir91Pass#'
        }

        self.user = get_user_model().objects.create_user(
            **self.user_data
        )

    def test_user_force_login(self):
        response = self.client.get('/persons/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)

        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        response = self.client.get('/persons/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_anonymous)


