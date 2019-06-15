from django.shortcuts import render
import article

# Create your views here.
def article(request):
    '''
    Render the article
    '''
    return render(request, 'article/article.html')