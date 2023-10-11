from django.shortcuts import render
from articles.services.main_services import MainActicleService

service = MainActicleService()

def main_template_with_articles(request):
    all_acticles = service.get_all_articles()
    return render(request, 'index.html', {'articles': all_acticles, 'menu': service.menu,
                                          'title': 'Главная страница'})

def main_template_get_article_by_id(request, pk):
    article = service.get_all_articles()
    return render(request, 'index.html', {'articles': article, 'menu': service.menu,
                                          'title': article.title})
