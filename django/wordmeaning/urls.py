from . import views
from .models import words
from django.conf.urls import url
urlpatterns = [
      url(r'^words/$', views.word_list),

]

