
from django.urls import path

from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
            # 目前还没有urls
            path('article-list/', views.article_list,name = 'article_list'),
            ]
