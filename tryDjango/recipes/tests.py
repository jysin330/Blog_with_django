from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Recipe, RecipeIngredient
User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        # create_user() is a custom model manager Method That only the user class has
        self.user_a = User.objects.create_user( "jyoti", password = '1234') 

    def test_user_pw (self):
        checked = self.user_a.check_password('1234')
        self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user( "jyoti", password = '1234') 

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)
    
    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_get.all()
        self.assertEqual(qs.count(), 0)