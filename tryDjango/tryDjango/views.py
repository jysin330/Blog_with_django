# to render html page
from django.http import HttpResponse
from articles.models import Article
import random

def home(request):
    # taking in a request(Django sends request)
    # return HTML response(We pick to return the response)
    number = random.randint(1,4)
    # from databases--->
    article_obj = Article.objects.get(id = number)
    
    # django templates--->
    Article_title = f''' <h1>{article_obj.title} (id : {article_obj.id})</h1>'''
    Article_content = f''' <h1>{article_obj.content}</h1>'''
    Html_string= Article_title +  Article_content
    return HttpResponse(Html_string)
