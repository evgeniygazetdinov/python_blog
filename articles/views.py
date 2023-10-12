from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from articles.serializer import ArticleSerializer
from articles.models import Articles


class ArticleAPIViewV1(APIView):
    """
    A view that returns a templated HTML representation of a given user.
    """

    def get(self, request, *args, **kwargs):
        articles = Articles.objects.all()
        return Response({'articles': ArticleSerializer(articles, many=True).data})

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            article = Articles.objects.filter(id=pk).get()
            if article:
                serializer = ArticleSerializer(instance=article, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({'updated_articles': serializer.data})
        else:
            return Response({'error': 'not accepted data'})

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            article = Articles.objects.filter(id=pk).get()
            if article:
                article.delete()
                return Response({'deleted_articles': pk})