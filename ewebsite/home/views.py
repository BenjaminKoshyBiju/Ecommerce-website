from django.shortcuts import render, get_object_or_404
from .models import Table1,Table2

# Create your views here.
table1_data = Table1.objects.all()  
table2_data = Table2.objects.all()
def index(request):
    return render(request,'index.html',{
        'table1_data': table1_data,
      
        })
def shop(request):
    return render(request,'shop.html')
def detail(request,table1_id):
    data = get_object_or_404(Table1, id=table1_id)
    table2_data=get_object_or_404(Table2, id=table1_id)
    return render(request,'detail.html',{'data': data,'table2_data': table2_data})
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')