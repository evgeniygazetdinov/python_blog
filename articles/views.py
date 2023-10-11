from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from articles.serializer import ArticleSerializer
from articles.models import Articles


class ArticleAPIView(APIView):
    """
    A view that returns a templated HTML representation of a given user.
    """

    def get(self, request, *args, **kwargs):
        articles = Articles.objects.all()
        return Response({'articles': ArticleSerializer(articles, many=True).data})

    def post(self, request, *args, **kwargs):
        # TODO fix validate
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': ArticleSerializer.data})

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            article = Articles.objects.filter(id=pk)
            serializer = ArticleSerializer(instance=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({'articles': ArticleSerializer.data})
    # def api_response(self, request):
