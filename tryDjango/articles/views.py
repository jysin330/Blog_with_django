from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Article
from .forms import ArticleForm
from django.http import Http404
def article_search_view(request):
    
    query_dict= request.GET #this is dictonary
    # query = query_dict.get('q') # <input type="text" name="q"/>
    try:
        query = int(query_dict.get('q'))
    except: 
        query =None
    article_obj =None
    if query is not None:
        article_obj = Article.objects.get(id =query)
        print(article_obj)
    else :
        article_obj ={}
    context= {
         'object' : article_obj
     }
    return render(request, 'articles/search.html', context = context)
    
    

@login_required    
def article_create_view(request):
    # query_dict = request.POST
    # print(query_dict)
    form = ArticleForm( request.POST or None)
    # print(dir(form))
    context ={
        'form' : form
    }
    if form.is_valid():
            article_object = form.save()
            context['form'] = ArticleForm()
            return redirect("article-detail", slug= article_object.slug)
            # title = form.cleaned_data.get("title")
            # content = form.cleaned_data.get("content")
            # print(title, content)
            # article_object = Article.objects.create(title = title, content= content)
            # context['object'] =article_object
            # context['created'] = True
    return render(request, "articles/create.html", context=context)


    #  form = ArticleForm()
    # # print(dir(form))
    # context ={
    #     'form' : form
    # }
    # if request.method == "POST":
        
    #     form = ArticleForm(request.POST)
    #     context['form'] = form
    #     if form.is_valid():
    #         title = form.cleaned_data.get("title")
    #         content = form.cleaned_data.get("content")
    #         print(title, content)
    #         article_object = Article.objects.create(title = title, content= content)
    #         context['object'] =article_object
    #         context['created'] = True
    # return render(request, "articles/create.html", context=context)


def article_detail_view(request , slug= None):
    
    article_obj =None
    if slug is not None:
        
        try:
            article_obj= Article.objects.get(slug = slug)
        # # except Article.DoesNotExist:
        # #     raise Http404
        # # except Article.MultipleObjectsReturned:
        # #     article_obj= Article.objects.filter(slug = slug).first()
        except:
            raise Http404
    context ={
        "object": article_obj
    }
    return render(request, "articles/detail.html", context=context)
