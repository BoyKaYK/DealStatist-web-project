from django.urls import path
from . import views

urlpatterns = [
    path('', views.deals,name='deals'),
    path('create', views.create,name='create'),
    path('createlink', views.create_with_link, name='createlink'),
    path('edit/<int>', views.edit, name='deals-edit'),
    path('delete/<id>', views.deal_delete, name='deal_delete'),
    path('check/<id>', views.check_sale, name='check_sale'),
    path('fix/<id>', views.fix_linked_deal, name='fix_linked_deal'),
    path('<id>', views.sold, name='deals-sold'),
    path('profit/calc', views.profit_calc, name='profit')
    

]

