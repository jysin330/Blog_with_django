import os
# from django.conf import settings
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password

class tryDjangoConfigTest(TestCase):
    def test_secret_key_strength(self):
        # self.assertTrue(1==2)
        # settings.SECRET_KEY
        # self.assertNotEqual('SECRET_KEY','abc123')
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        try:
            is_strong = validate_password(SECRET_KEY)
            
        except Exception as e:
            msg= f"weak secret key - {e.messages}"
            self.fail(msg)