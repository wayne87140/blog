from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Page
# Create your views here.

# def main(request):
#     '''
#     Show 'Hello world!' in the main page
#     '''
#     return HttpResponse('Hello world!')


def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django is awesome'}
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about Page
    '''
    return render(request, 'main/about.html')