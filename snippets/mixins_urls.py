from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import mixins_views

urlpatterns = [
    path('snippets/', mixins_views.SnippetList.as_view()),
    path('snippets/<int:pk>/', mixins_views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
