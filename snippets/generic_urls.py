from rest_framework.urlpatterns import format_suffix_patterns
from snippets import generic_views
from django.urls import path, include

urlpatterns = [
    path('root/', generic_views.api_root),
    path('snippets/', generic_views.SnippetList.as_view(),name='snippet-list'),
    path('snippets/<int:pk>/', generic_views.SnippetDetail.as_view(),name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', generic_views.SnippetHighlight.as_view(),name='snippet-highlight'),
    path('users/', generic_views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', generic_views.UserDetail.as_view(),name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
