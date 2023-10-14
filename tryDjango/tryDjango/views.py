from articles.models import Article

# to render html page
from django.http import HttpResponse
from django.template.loader import render_to_string
# from django.template.loader import render_to_string, get_template
import random

def home(request):
    # taking in a request(Django sends request)
    # return HTML response(We pick to return the response)
    number = random.randint(1,4)
    print(id)
    # from databases--->
    article_obj = Article.objects.get(id = number)
    article_list = Article.objects.all()
    my_queryset= article_list #[67,277,383,4773,383]
    # mylist_str =""
    # for x in my_list:
    #     mylist_str += f"the number is {x}\n"
    context={
        'object_list': my_queryset,
        'object': article_obj,
        'title': article_obj.title,
        "content" : article_obj.content,
        "id": article_obj.id
    }
    
    # django templates--->
    
    #  direct method
    # Article_title = f''' <h1>{article_obj.title} (id : {article_obj.id})</h1>'''
    # Article_content = f''' <h1>{article_obj.content}</h1>'''
    # Html_string= Article_title +  Article_content
    # return HttpResponse(Html_string)
    
    #  by format method
    # HTML_string= """ <h1>{title} (id : {id})</h1> 
    # <h1>{content}</h1>""".format(**context)
    
    # get_template method
    # tmpl = get_template('home.html') 
    # temp_string = tmpl.render(context= context)
    
    # render_to_string method 
    HTML_string= render_to_string('home.html', context= context)
    return HttpResponse(HTML_string)
