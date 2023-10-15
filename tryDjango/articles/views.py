from django.shortcuts import render

# Create your views here.
from .models import Article
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
    
    
def article_detail_view(request , id= None):
    
    article_obj =None
    if id is not None:
        article_obj= Article.objects.get(id = id)
        
    context ={
        "object": article_obj
    }
    return render(request, "articles/detail.html", context=context)
