from apt.progress.text import _
from django.conf.urls import url
from django.urls import path

from polls.views import LoginView
from . import views

app_name = 'polls'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]