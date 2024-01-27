from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        # create_user() is a custom model manager Method That only the user class has
        self.user_a = User.objects.create_user( "jyoti", password = '1234') 

    def test_user_pw (self):
        checked = self.user_a.check_password('1234')
        self.assertTrue(checked)