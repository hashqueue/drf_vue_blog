from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer, ArticleDetailSerializer


# Create your views here.
class ArticleView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
