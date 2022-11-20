from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Client(models.Model):
    name = models.CharField(_("Nombre"), null=False, blank=False, max_length=40)
    last_name = models.CharField(_("Apellido"), null=False, blank=False, max_length=40)
    document_type = models.CharField(_("Tipo de documento"), null=False, blank=False, max_length=40, choices=[
        ('Tarjeta de identidad', 'Tarjeta de identidad'),
        ('Cédula de ciudadanía', 'Cédula de ciudadanía'),
        ('Tarjeta de extranjería', 'Tarjeta de extranjería'),
        ('Cédula de extranjería', 'Cédula de extranjería'),
        ('Pasaporte', 'Pasaporte'),
        ('Otro', 'Otro')
    ])
    document_number = models.CharField(_("Número de documento"), null=False, blank=False, max_length=20)
    date_joined = models.DateTimeField(_("Fecha de ingreso"), default=timezone.now)

    def __str__(self): 
        return self.document_number
    
class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=False)
    payment_type = models.CharField(_("Tipo de pago"), null=False, blank=False, max_length=40, choices=[
        ('Sesión', 'Sesión'),
        ('Semana', 'Semana'),
        ('Quincena', 'Quincena'),
        ('Mes', 'Mes')
    ])
    total = models.IntegerField(_("Total"), null=False, blank=False)
    status = models.CharField(_("Estado"), null=False, blank=False, max_length=40, choices=[
        ('Pago', 'Pago'),
        ('Pendiente', 'Pendiente')
    ])
    date_created = models.DateTimeField(_("Fecha de creación"), default=timezone.now)
    date_joined = models.DateField(_("Fecha"))