from django.urls import path
from . import views

urlpatterns = [
    path('retail/zinvtd/', views.stock, name='zinvtd'),
    path('retail/zinvtd/material_matchcode/', views.material_matchcode, name='material_matchcode'),
    path('retail/zinvtd/article_grp_matchcode/', views.article_grp_matchcode, name='article_grp_matchcode'),
]