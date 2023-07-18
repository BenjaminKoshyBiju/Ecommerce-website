from django.shortcuts import render, get_object_or_404,redirect
from .models import Table1,Table2,Cart

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
    if request.method=='POST':
        name = data.name
        price = data.price
        img = data.img
        
        cart = Cart(name=name,price=price,img=img)
        cart.save()
        print("saved successfully")
        return redirect('cart.html')
    else:     
        return render(request,'detail.html',{'data': data,'table2_data': table2_data})
def cart(request,table1_id):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')