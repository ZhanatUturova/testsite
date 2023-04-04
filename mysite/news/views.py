from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category

# Create your views here.
# def index(request):
#     news = News.objects.all()
#     res = '<h1>Список новостей</h1>'
#     for item in news:
#         res += f'<div>\n<h3>{item.title}</h3>\n<p>{item.content}</p>\n</div>\n<hr>'
#     return HttpResponse(res)

def index(request):
    # news = News.objects.order_by('-created_at')   # теперь сортировка прописана в моделях
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, template_name='news/category.html', context=context)