#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from six import python_2_unicode_compatible


class Company(models.Model):
    name = models.CharField(max_length=150)
    bic = models.CharField(max_length=150, blank=True)

    #Reduce SQL queries by using len function instead of looping through order queries and adding 1
    def get_order_count(self):
        orders = len(self.orders.all())
        return orders
        # orders = 0
        # for order in self.orders.all():
        #     order += 1
        # return orders


    # Removed get_order_sum all together as this method causes too many queries, 
    # replaced with annotate on company_list query on views.py to reduce database queries

    # def get_order_sum(self):
    #     total_sum = 0
    #     for contact in self.contacts.all():
    #         for order in contact.orders.all():
    #             total_sum += order.total
    #     return total_sum

    #Added to see live data instead of "<QuerySet>" when debugging 
    def __str__(self):
        return self.name
        


class Contact(models.Model):
    company = models.ForeignKey(Company, related_name="contacts", on_delete=models.PROTECT)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()


    # Redundant model method, that causes too many SQL queries, 
    # simplified and re-use method in Company model

    # def get_order_count(self):
        # orders = 0
        # for order in self.orders.all():
        #     order += 1
        # return orders
    
    #Added to see live data instead of "<QuerySet>" when debugging 
    def __str__(self):
        return self.first_name + " " + self.last_name + ' with ' + self.company.name




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

    #Added to see live data instead of "<QuerySet>" when debugging 
    def __str__(self):
        return "Order # " + self.order_number + ' for ' +self.company.name
