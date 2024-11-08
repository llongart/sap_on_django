from django.urls import path
from . import views

urlpatterns = [
    path('retail/zinvtd/', views.stock, name='zinvtd')
]