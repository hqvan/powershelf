from django.conf.urls import url
from main_app.views import index

urlpatterns = [
    url(r'^$', index),
]