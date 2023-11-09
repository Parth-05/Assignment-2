# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('scatter_plot/', views.generate_scatter_plot, name='scatter_plot'),
    path('bar_chart/', views.generate_bar_chart, name='bar_chart'),
    
]
