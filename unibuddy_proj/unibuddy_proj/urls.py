from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import search_app.urls as se_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include(se_urls)),
]
