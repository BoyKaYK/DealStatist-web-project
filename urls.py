from django.urls import path
from . import views

urlpatterns = [
    path('', views.deals,name='deals'),
    path('create', views.create,name='create'),
    path('edit/<int>', views.edit, name='deals-edit'),
    path('<id>', views.sold, name='deals-sold'),
    path('profit/calc', views.profit_calc, name='profit')
]

