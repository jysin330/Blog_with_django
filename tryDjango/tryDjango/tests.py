import os
# from django.conf import settings
from django.test import TestCase

class tryDjangoConfigTest(TestCase):
    def test_secret_key_strength(self):
        # self.assertTrue(1==2)
        # settings.SECRET_KEY
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        self.assertNotEqual('SECRET_KEY','abc123')