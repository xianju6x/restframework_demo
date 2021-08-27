from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import viewset_views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', viewset_views.SnippetViewSet)
router.register(r'users', viewset_views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
