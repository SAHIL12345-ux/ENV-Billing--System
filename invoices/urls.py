from django.urls import path # type: ignore
from .import views

urlpatterns = [
    path('',views.invoice_list,name='invoice_list'),
    path('create/', views.create_invoice, name='create_invoice'),
    path('update/<int:id>/', views.invoice_update, name='invoice_update'),   
    path('delete/<int:id>/', views.invoice_delete, name='invoice_delete'),
]


