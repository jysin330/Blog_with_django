from django.db import models
from django.db.models.signals import pre_save, post_save
# from django.utils import timezone
from django.urls import reverse
# Create your models here.
from django.shortcuts import redirect
from .utils import slugify_instance_title

class Article(models.Model):
    title = models.CharField(max_length= 70)
    slug = models.SlugField(unique =True,null= True, blank = True)
    content = models.TextField()
    timestamp =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # publish =models.DateField(auto_now_add = False, auto_now= False, default = timezone.now)
    publish =models.DateField(auto_now_add = False, auto_now= False, null = True, blank = True)
    def get_absolute_url(self):
        pass

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
