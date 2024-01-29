from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Recipe, RecipeIngredient
User = get_user_model()
from django.core.exceptions import ValidationError
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
        self.recipe_a = Recipe.objects.create(
            name = "Grilled Chicken", 
            user = self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name = "Grilled Chicken Tacos", 
            user = self.user_a
        )
        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            recipe = self.recipe_a,
            name = "Chicken",
            quantity = '1/2',
            unit ='pound',
        )


    def test_user_count(self):
        qs = User.objects.all()
        
        self.assertEqual(qs.count(), 1)
    
    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user = user)
        
        self.assertEqual(qs.count(), 2)

    def test_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()
       
        self.assertEqual(qs.count(), 1)

    def test_recipe_ingredient_forward_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe= recipe)
        self.assertEqual(qs.count(), 1)

    def test_user_two_level_relation(self):
        user =self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user = user)
        # Three level
        # qs = RecipeIngredient.objects.filter(recipeingredient__recipe__user = user)
        
        self.assertEqual(qs.count(), 1)

    def test_user_two_level_relation_reverse(self):
        user =self.user_a
        recipeIngredient_ids = list(user.recipe_set.all().values_list('recipeingredient', flat = True))
        qs = RecipeIngredient.objects.filter(id__in = recipeIngredient_ids)
        self.assertEqual(qs.count(), 1)

    def test_user_two_level_relation_via_recipes(self):
        user =self.user_a
        ids = user.recipe_set.all().values_list('id', flat = True)
        qs = RecipeIngredient.objects.filter(recipe__id__in = ids)
        self.assertEqual(qs.count(), 1)

    def test_unit_measure_validation(self):
        invalid_unit ='ounce'
        
        ingredient = RecipeIngredient(
                name = 'New',
                quantity = 10,
                recipe = self.recipe_a,
                unit = invalid_unit,
            )
        ingredient.full_clean()

    def test_unit_measure_validation_error(self):
        invalid_unit =['nada', 'havad']
        with self.assertRaises(ValidationError):
            for unit in invalid_unit:
                ingredient = RecipeIngredient(
                    name = 'New',
                    quantity = 10,
                    recipe = self.recipe_a,
                    unit = unit,
                )
                ingredient.full_clean()