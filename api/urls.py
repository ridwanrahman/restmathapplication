from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^equation$', Equation.as_view()),
]