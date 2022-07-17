from django.urls import path

from . import views
app_name = 'budget_app'
urlpatterns = [
    
    #Index page
    path('', views.index, name = "index"),
    path('transactions/', views.transactions, name='transactions'),
    path('transactions/<int:transaction_id>/', views.transaction, name='transaction'),
    path('new_entry/<int:transaction_id>/', views.new_entry, name='new_entry'),
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry')
]