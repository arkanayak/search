from django.conf.urls import url
from search_app.views import preprocess, process_queries

urlpatterns = [
    url(r'preprocess', preprocess),
    url(r'process_queries', process_queries)
]
