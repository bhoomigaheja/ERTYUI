from django.http import HttpResponse
from django.shortcuts import render
from jobspark.main import main

def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')


def signn(request):
    return render(request,'sing-up.html')

def sign(request):
    return render(request,'sign-in.html')


def pricing(request):
    return render(request,'pricing.html')


def forgot(request):
    return render(request,'forgot.html')
def contact(request):
    return render(request,'contact.html')

def jobs_view(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        if query:
            
            scraped_data = main(query)
            context = {'data': scraped_data,}
            return render(request, 'jobs.html', context)
    return render(request, 'templates\jobs.html')