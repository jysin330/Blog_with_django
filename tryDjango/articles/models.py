from django.db import models
from django.db.models.query import QuerySet
from django.db.models.signals import pre_save, post_save
# from django.utils import timezone
from django.urls import reverse
# Create your models here.
from django.shortcuts import redirect
from .utils import slugify_instance_title
from django.db.models import Q
from django.conf import settings

User = settings.AUTH_USER_MODEL
class ArticleQuerySet(models.QuerySet):
    def search(self,query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)
class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    
    def search(self,query=None):
        return self.get_queryset().search(query=query)
    # def search(self,query=None):
    #     if query is None or query == "":
    #         return self.get_queryset().none()
    #     lookups = Q(title__icontains=query) | Q(content__icontains=query)
    #     return self.get_queryset().filter(lookups)
        # return Article.objects.filter(lookups)

class Article(models.Model):
    user = models.ForeignKey(User, blank =True , null =True , on_delete =models.SET_NULL)
    title = models.CharField(max_length= 70)
    slug = models.SlugField(unique =True,null= True, blank = True)
    content = models.TextField()
    timestamp =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish =models.DateField(auto_now_add = False, auto_now= False, null = True, blank = True)

    objects = ArticleManager()

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs ={"slug": self.slug})
        # return reverse("article-create")
        # pass

    def save(self,*args, **kwargs):
        # obj = Article.objects.get(id=1)
        # set something
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        #     self.save()
        # obj.save()
        # do another something

def article_presave(sender,instance, *args,**kwargs):
    # print("pre save: ")
    # print(sender,instance)
    if instance.slug is None:
        # instance.slug = slugify(instance.title)
        slugify_instance_title(instance, save= False)
    
    # instance.slug = slugify(instance.title)

pre_save.connect(article_presave, sender= Article)

def article_postsave(sender, instance, created, *args,**kwargs):
    # print("post save: ")
    # print(args, kwargs)
    if created:
        slugify_instance_title(instance, save= True)
        # instance.slug ="this is the slug"
        # instance.save()

post_save.connect(article_postsave, sender= Article)
