from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import api_views

urlpatterns = [
    path('snippets/', api_views.SnippetList.as_view()),
    path('snippets/<int:pk>/', api_views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
