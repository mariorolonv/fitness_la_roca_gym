from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.mixins import GroupRequiredMixin
from users.models import Client
from .forms import *
from django.db.models import Q
import datetime

@login_required
def home(request):
    return render(request, 'users/dashboard.html')

class Logout(LoginRequiredMixin, LogoutView):
    pass


def register(request):
    data = {
        'form':RegisterForm()
    }
    if request.method == 'POST':
        formulario = RegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    return render(request, "registration/sign_up.html", data)

    

class ClientsView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    group_required = ['Moderators']
    login_url = reverse_lazy('login')
    template_name = "users/clients.html"
    
    def get(self, request):
        week_dates = []
        now = datetime.datetime.now()
        actual = now.strftime("%Y-%m-%d")
        month = now.strftime("%Y-%m")
        
        day = now.day
        month1 = now.month
        
        for i in range(0,now.weekday()):
            day = datetime.datetime.now() - datetime.timedelta(days=i+1)
            month1 = day.month
            day = day.day
            if len(str(month1)) == 1:
                month1 = "0{}".format(month1)
            if len(str(day)) == 1:
                day = "0{}".format(day)
            ant = "{}-{}-{}".format(now.year,month1,day)
            week_dates.insert(0,ant)
        week_dates.append(actual)
        end_date = datetime.datetime.now() + datetime.timedelta(days=1)
        
        clients_day = Client.objects.filter(date_joined__day=now.day,date_joined__month=now.month,date_joined__year=now.year).order_by("-date_joined")
        clients_month = Client.objects.filter(date_joined__contains=month).order_by("-date_joined")
        clients_week = Client.objects.filter(date_joined__range=(week_dates[0], end_date)).order_by("-date_joined")
        clients = Client.objects.all().order_by('-date_joined')
        list_clients = len(clients)
        list_day = len(clients_day) 
        list_month = len(clients_month) 
        list_week = len(clients_week) 
        
        return render(request, self.template_name, {"clients":clients,"clients_day":clients_day,"clients_month":clients_month,"clients_week":clients_week, "list_clients":list_clients, "list_day":list_day, "list_month":list_month, "list_week":list_week})
    
    def post(self, request):
        if request.POST:
            filters = {}
            document_number = request.POST.get('search_document_number', None)
            if document_number and document_number.isdigit():
                filters['document_number__icontains'] = document_number
            clients = Client.objects.filter(Q(**filters)).order_by('-date_joined')
            list_clients = len(clients) 
            
        else:
            clients = Client.objects.all().order_by('-date_joined')
        return render(request, "users/clients.html", {"clients":clients, "list_clients":list_clients})
    
class FormClientView(HttpRequest):
    @login_required
    def index(request):
        client = FormClient()
        return render(request, "users/add_client.html", {"form":client})
    
    @login_required
    def process_client(request):
        client = FormClient(request.POST)
        if client.is_valid():
            client.save()
            client = FormClient()
            
        return render(request, "users/add_client.html", {"form":client, "message": 'OK'})
    
    @login_required
    def edit(request, id_client):
        client = Client.objects.filter(id=id_client).first()
        form = FormClient(instance=client)
        return render(request, "users/edit_client.html", {"form":form, 'client':client})
    
    @login_required
    def update(request, id_client):
        client = Client.objects.get(pk=id_client)
        form = FormClient(request.POST, instance=client)
        if form.is_valid():
            form.save()
        return redirect("users:clients")
    
class DeleteClientView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = ['Moderators']
    login_url = reverse_lazy('login')
    model = Client
    template_name = "users/delete_client.html"
    success_url = reverse_lazy('users:clients')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('users:clients')
        return context
    
    
class InvoicesView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    group_required = ['Moderators']
    login_url = reverse_lazy('login')
    template_name = "invoices/invoices.html"
    
    def get(self, request):
        week_dates = []
        now = datetime.datetime.now()
        actual = now.strftime("%Y-%m-%d")
        month = now.strftime("%Y-%m")
        
        day = now.day
        month1 = now.month
        
        for i in range(0,now.weekday()):
            day = datetime.datetime.now() - datetime.timedelta(days=i+1)
            month1 = day.month
            day = day.day
            if len(str(month1)) == 1:
                month1 = "0{}".format(month1)
            if len(str(day)) == 1:
                day = "0{}".format(day)
            ant = "{}-{}-{}".format(now.year,month1,day)
            week_dates.insert(0,ant)
        week_dates.append(actual)
        end_date = datetime.datetime.now() + datetime.timedelta(days=1)
        
        clients = Client.objects.all().order_by('-date_joined')
        invoices_day = Invoice.objects.filter(date_created__day=now.day,date_created__month=now.month,date_created__year=now.year).order_by("-date_created")
        invoices_month = Invoice.objects.filter(date_created__contains=month).order_by("-date_created")
        invoices_week = Invoice.objects.filter(date_created__range=(week_dates[0], end_date)).order_by("-date_created")
        invoices = Invoice.objects.all().order_by('-date_created')
        list_invoices = len(invoices)
        list_day = len(invoices_day) 
        list_month = len(invoices_month) 
        list_week = len(invoices_week) 
        
        return render(request, self.template_name, {"clients":clients, "invoices":invoices,"invoices_day":invoices_day,"invoices_month":invoices_month,"invoices_week":invoices_week, "list_invoices":list_invoices, "list_day":list_day, "list_month":list_month, "list_week":list_week})
    
    def post(self, request):
        if request.POST:
            document_number = request.POST.get('search_document_number', None)
            status = request.POST.get('search_status', None)
            invoices = Invoice.objects.filter(Q(client_id__in = document_number) | Q(status=status))
            list_invoices = len(invoices) 
        else:
            invoices = Invoice.objects.all().order_by('-date_created')
        return render(request, "invoices/invoices.html", {"invoices":invoices, "list_invoices":list_invoices})
    
class FormInvoiceView(HttpRequest):
    @login_required
    def detail(request, id_invoice):
        invoice = Invoice.objects.filter(id=id_invoice).first()
        form = FormInvoice(instance=invoice)
        return render(request, "invoices/detail_invoice.html", {"form":form, 'invoice':invoice})
    
    @login_required
    def index(request):
        invoice = FormInvoice()
        clients = Client.objects.all().order_by('-date_joined')
        return render(request, "invoices/add_invoice.html", {"form":invoice, "clients":clients})
    
    @login_required
    def process_invoice(request):
        invoice = FormInvoice(request.POST)
        clients = Client.objects.all().order_by('-date_joined')
        if invoice.is_valid():
            invoice.save()
            invoice = FormInvoice()
            
        return render(request, "invoices/add_invoice.html", {"form":invoice, "clients":clients, "message": 'OK'})
    
    @login_required
    def edit(request, id_invoice):
        invoice = Invoice.objects.filter(id=id_invoice).first()
        form = FormEditInvoice(instance=invoice)
        clients = Client.objects.all().order_by('-date_joined')
        return render(request, "invoices/edit_invoice.html", {"form":form, "clients":clients, 'invoice':invoice})
    
    @login_required
    def update(request, id_invoice):
        invoice = Invoice.objects.get(pk=id_invoice)
        form = FormEditInvoice(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
        return redirect("users:invoices")
    
class DeleteInvoiceView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = ['Moderators']
    login_url = reverse_lazy('login')
    model = Invoice
    template_name = "invoices/delete_invoice.html"
    success_url = reverse_lazy('users:invoices')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una factura'
        context['entity'] = 'Facturas'
        context['list_url'] = reverse_lazy('users:invoices')
        return context