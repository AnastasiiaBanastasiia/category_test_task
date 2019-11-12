from django.urls import path, include
from rest_framework.routers import SimpleRouter

from categories import views

router = SimpleRouter()
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
