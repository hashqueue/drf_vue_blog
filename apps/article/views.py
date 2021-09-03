from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer, ArticleDetailSerializer
from .permissions import IsAdminOrReadOnly


# Create your views here.
class ArticleView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
