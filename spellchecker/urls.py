
from django.urls import path
from .views import InsertWordView, SearchWordView, StartsWithView, PopulateTrieView

urlpatterns = [
    path('populate-trie/', PopulateTrieView.as_view(), name='populate-trie'),
    path('insert/', InsertWordView.as_view(), name='insert_word'),
    path('search/', SearchWordView.as_view(), name='search_word'),
    path('startswith/', StartsWithView.as_view(), name='starts_with'),
]
