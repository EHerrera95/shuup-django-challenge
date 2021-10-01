#-*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import  render
from django.db.models import Sum
from django.db.models.functions import Coalesce
# Create your views here.
# from django.views.generic import ListView


from mailer.models import Company, Contact, Order

# As mentioned in the urls.py, I just prefer to use function based views over class views

# class IndexView(ListView):
#     template_name = "mailer/index.html"
#     model = Company
#     paginate_by = 100

def index(request):

    #Company and Contact Query Sets using prefetch and selected related to optimize SQL queries on template
    company_list = Company.objects.prefetch_related('contacts','orders').annotate(order_total=Sum('orders__total')) #Replacing get_order_sum and passing to template as order_total to reduce SQL queries
    contact_list = Contact.objects.select_related('company') 
    
    #Pagination in the function based view
    paginator = Paginator(company_list, 100)
    page=request.GET.get('page')  
    try: 
        company_list = paginator.page(page)
    except PageNotAnInteger:
        company_list = paginator.page(1)
    except EmptyPage:
        company_list = paginator.page(paginator.num_pages)

    return render(request, 'mailer/index.html', {
        'page': page, 
        'company_list': company_list,
        'contact_list': contact_list,
        })
