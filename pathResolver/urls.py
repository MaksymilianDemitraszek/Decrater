from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PathResolverView.as_view()),
    path('safe/', views.PathResolverViewSafe.as_view()),

]