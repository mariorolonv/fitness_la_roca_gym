from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import *

app_name = 'users'
urlpatterns = [
    path("sign_up/", register, name="sign_up"),
    path('dashboard/', home, name='dashboard'),
    path('clients/', ClientsView.as_view(), name='clients'),
    path('add_client/', FormClientView.index, name='add_client'),
    path('process_client/', FormClientView.process_client, name='process_client'),
    path('edit_client/<int:id_client>', FormClientView.edit, name='edit_client'),
    path('update_client/<int:id_client>', FormClientView.update, name='update_client'),
    path('delete_client/<int:pk>', DeleteClientView.as_view(), name='delete_client'),
    path('invoices/', InvoicesView.as_view(), name='invoices'),
    path('detail_invoice/<int:id_invoice>', FormInvoiceView.detail, name='detail_invoice'),
    path('add_invoice/', FormInvoiceView.index, name='add_invoice'),
    path('process_invoice/', FormInvoiceView.process_invoice, name="process_invoice"),
    path('edit_invoice/<int:id_invoice>', FormInvoiceView.edit, name='edit_invoice'),
    path('update_invoice/<int:id_invoice>', FormInvoiceView.update, name='update_invoice'),
    path('delete_invoice/<int:pk>', DeleteInvoiceView.as_view(), name='delete_invoice'),
    path("logout/", Logout.as_view(), name="logout"),
]