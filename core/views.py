from django.shortcuts import render
from .forms import RestaurantForm
from .models import Restaurant,Sale,Rating,Staff,StaffRestaurant
Staff
from django.db.models import Sum,Prefetch,Q,F
from django.utils import timezone

# Create your views here.

def index(request):
    name_has_num = Q(restaurant__name__regex = r"[0-9]+")
    profited = Q(income__gt = F('expenditure'))

    sales = Sale.objects.select_related('restaurant').filter(name_has_num|profited)
    print(sales)
    return render(request,'index.html')
    