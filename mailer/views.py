#-*- coding: utf-8 -*-
# from django.core import paginator
from django.core.paginator import Page, Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView


from mailer.models import Company, Contact, Order


# class IndexView(ListView):
#     template_name = "mailer/index.html"
#     model = Company
#     context_object_name ='company_list'
    
#     company_dict={}
#     temp_dict={}
#     all_companies = Company.objects.all()
#     for a in all_companies:
#         temp_dict = {'name' : a.name, 'order_count' : a.get_order_count(), 'order_sum': a.get_order_sum()}
#         print(temp_dict)

#     paginate_by = 100

#     # def get_context_data(self, *args, **kwargs):
#     #     context = super(IndexView, self).get_context_data(*args, **kwargs)
#     #     context['company_list'] = temp_dict

def index(request):
    company_list = Company.objects.all()
    paginator = Paginator(company_list, 100)
    page=request.GET.get('page')
    try: 
        company_list = paginator.page(page)
    except PageNotAnInteger:
        company_list = paginator.page(1)
    except EmptyPage:
        company_list = paginator.page(paginator.num_pages)
    
    return render(request, 'mailer/index.html', {'page': page, 'company_list': company_list})
