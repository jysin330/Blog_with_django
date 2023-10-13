# to render html page
from django.http import HttpResponse
HTML_String = ''' <h1>Hello World</h1>'''


def home(request):
    # taking in a request(Django sends request)
    # return HTML response(We pick to return the response)
    return HttpResponse(HTML_String)
