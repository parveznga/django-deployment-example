from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text' : 'This is custom filters example', 'number' : 100}
    return render(request,'web_app/index.html',context_dict)

def other(request):
    return render(request,'web_app/other.html')

def relative(request):
    return render(request,'web_app/relative_url_templates.html')
