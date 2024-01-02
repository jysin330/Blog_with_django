from django.db import models
from django.db.models.signals import pre_save, post_save
# from django.utils import timezone
from django.utils.text import slugify
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length= 70)
    slug = models.SlugField(null= True, blank = True)
    content = models.TextField()
    timestamp =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # publish =models.DateField(auto_now_add = False, auto_now= False, default = timezone.now)
    publish =models.DateField(auto_now_add = False, auto_now= False, null = True, blank = True)

    def save(self,*args, **kwargs):
        # obj = Article.objects.get(id=1)
        # set something
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        #     self.save()
        # obj.save()
        # do another something

def article_presave(*args,**kwargs):
    print("pre save: ")
    print(args, kwargs)

pre_save.connect(article_presave, sender= Article)

def article_postsave(*args,**kwargs):
    print("post save: ")
    print(args, kwargs)

post_save.connect(article_postsave, sender= Article)
