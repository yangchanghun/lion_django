from . models import Post
from django.urls import path
from . import views
app_name = "blog"


urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
]