from django.shortcuts import render
from .models import Table1,Table2
# Create your views here.
table1_data = Table1.objects.all()  
table2_data = Table2.objects.all()
def index(request):
    return render(request,'index.html',{
        'table1_data': table1_data,
        'table2_data': table2_data,
        })
def shop(request):
    return render(request,'shop.html')
def detail(request):
    return render(request,'detail.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')