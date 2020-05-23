from django.conf.urls import url
from search_app.views import preprocess

urlpatterns = [
    url(r'preprocess', preprocess),
]
