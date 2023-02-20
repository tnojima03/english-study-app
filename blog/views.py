from django.shortcuts import render
from blog.models import Article
from django.core.paginator import Paginator

def index(request):
    objs = Article.objects.all()
    pagenator = Paginator(objs, 2)
    page_number = request.GET.get('page')
    context = {
        #'articles': objs,
        'page_obj': pagenator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'blog/blogs.html', context)

def article(request, pk):
    obj = Article.objects.get(pk=pk)
    context = {
        'article': obj,
    }

    return render(request, 'blog/article.html', context)