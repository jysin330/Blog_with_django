from django.shortcuts import render , redirect, get_object_or_404
# CRUD -> Create Retrieve Update Delete
# Create your views here.
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm,RecipeIngredientForm
@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user = request.user)
    context ={
        "object_list": qs
                }
    return render(request, "recipes/list.html", context)


@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe,id = id, user = request.user)
    context ={
        'object': obj
    }
    return render(request, "recipes/detail.html", context)


@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context ={
        'form': form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe,id = id, user = request.user)
    # form = RecipeForm(request.POST or None, initial={"name": "This is wrong data"})
    form = RecipeForm(request.POST or None, instance=obj)
    form_2 = RecipeIngredientForm(request.POST or None)
    context ={
        'form': form,
        'form_2': form_2,
        'object': obj
    }
    if all([form.is_valid(),form_2.is_valid()]):
        parent=form.save(commit=False)
        parent.save()
        child= form_2.save(commit=False)
        child.recipe = parent
        child.save()

        
       
        context['message']= 'Data Saved.'
    return render(request, "recipes/create-update.html", context)