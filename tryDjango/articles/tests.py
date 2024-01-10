from django.test import TestCase

# Create your tests here.
from .models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title ="hello world", content="another hello world content")

    def test_querySet_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())


    def test_querySet_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(),1)