from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PathLoggerView.as_view()),
    path('safe/', views.PathLoggerView.as_view()),
]