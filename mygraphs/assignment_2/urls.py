# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('countour_plot/', views.generate_countour_plot, name='scatter_plot'),
    path('area_chart/', views.generate_area_chart, name='bar_chart'),
    
]
