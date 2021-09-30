#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from six import python_2_unicode_compatible


class Company(models.Model):
    name = models.CharField(max_length=150)
    bic = models.CharField(max_length=150, blank=True)

    def get_order_count(self):
        orders = 0
        for order in self.orders.all():
            orders += 1
        return orders

    def get_order_sum(self):
        total_sum = 0
        all_contacts = self.contacts.all()
        for contact in all_contacts:
            all_orders = contact.orders.all()
            for order in all_orders:
                total_sum += order.total
        return total_sum


class Contact(models.Model):
    company = models.ForeignKey(Company, related_name="contacts", on_delete=models.PROTECT)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()

    def get_order_count(self):
        orders = 0
        all_orders = self.orders.all()
        for order in all_orders:
            orders += 1
        return orders


@python_2_unicode_compatible
class Order(models.Model):
    order_number = models.CharField(max_length=150)
    company = models.ForeignKey(Company, related_name="orders", on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, related_name="orders", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=18, decimal_places=9)
    order_date = models.DateTimeField(null=True, blank=True)
    # for internal use only
    added_date = models.DateTimeField(auto_now_add=True)
    # for internal use only
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.order_number
