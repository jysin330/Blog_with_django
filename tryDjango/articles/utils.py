import random
from django.utils.text import slugify

# SLugify the instance of the Article
def slugify_instance_title(instance, save= False, new_slug = None):
    if new_slug is not None:
        slug =new_slug
    else:
        slug_remove_space = slugify(instance.title)
        slug= slug_remove_space.replace(" ","")

    Klass = instance.__class__
    qs = Klass.objects.filter(slug = slug).exclude(id =instance.id)
    # qs = Article.objects.filter(slug = slug).exclude(id =instance.id)
    if qs.exists():
        slug = f"{slug} - {random.randint(300_000,500_000)}"
        # slug = f"{slug} - {qs.count()+1}"
        return slugify_instance_title(instance, save=save,new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()

    return instance