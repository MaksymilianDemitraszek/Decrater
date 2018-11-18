from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('<int:last>/', views.PathLoggerView.as_view()),
    path('', views.PathLoggerView.as_view())
]