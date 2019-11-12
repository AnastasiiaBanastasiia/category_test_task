from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
