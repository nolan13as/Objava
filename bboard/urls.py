from django.conf.urls import url
from django.contrib.staticfiles.urls import static
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import index, by_rubric, BbCreateView
from django.conf import settings

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
]
