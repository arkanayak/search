from django.conf.urls import url
from search_app.views import preprocess, search_queries

urlpatterns = [
    url(r'preprocess', preprocess),
    url(r'search_queries', search_queries)
]
