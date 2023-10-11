from articles.models import Articles

class MainActicleService:
    """ все работа по статьям"""
    menu = ['о сайте', 'каталог статей', 'стать автором']

    def get_all_articles(self):
        return Articles.objects.all()

    def get_specific_sev(self, pk):
        return Articles.objects.filter(id=pk)