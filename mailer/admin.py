#-*- coding: utf-8 -*-
from mailer.models import Company, Contact, Order
from django.contrib import admin

# Register your models here.
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Order)
