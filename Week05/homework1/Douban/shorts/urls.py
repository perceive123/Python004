from django.urls import path,re_path
from . import views

urlpatterns = [
    # re_path(r'shorts?q=(?P<q>\w+)',views.shorts_q),
    path('', views.index),
    path('shorts', views.shorts),
]