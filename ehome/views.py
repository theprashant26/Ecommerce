from django.shortcuts import render, redirect
from .models import *
from django.views import View
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Productcategory(View):
    def get(self, request):
        Top_Savers_Today = Product.objects.filter(category='TSP')
        Best_Offer = Product.objects.filter(category='BO')
        return render(request, 'ehome/index.html', {'Top_Savers_Today':Top_Savers_Today,'Best_Offer':Best_Offer})
    
@login_required
def address(request):
    add = customer.objects.filter(user=request.user)
    return render(request, 'ehome/address.html',{'add':add})

@login_required
def MyCart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    cart(user=user, product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cartt = cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 80.0
        total_amount = 0.0
        cart_product = [p for p in cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request,'ehome/addtocart.html', {'carts':cartt, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request, 'ehome/emptycart.html')

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 80.0
        cart_product = [p for p in cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 80.0
        cart_product = [p for p in cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 80.0
        cart_product = [p for p in cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'amount':amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)



def blog(request):
    return render(request, 'ehome/blog.html')
def blogdetail(request):
    return render(request, 'ehome/blog-detail.html')

@login_required
def checkout(request):
    user = request.user
    add = customer.objects.filter(user=user)
    cart_items = cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 80.0
    totalamount = 0.0
    cart_product = [p for p in cart.objects.all() if p.user == request.user]
    if cart_product :
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount +shipping_amount

    return render(request, 'ehome/checkout.html', {'add':add, 'totalamount':totalamount,'cart_items':cart_items})

def contact(request):
    return render(request, 'ehome/contact.html')

@login_required
def orderlist(request):
    op = Orderplaced.objects.filter(user=request.user)
    return render(request, 'ehome/orderlist.html', {'order_placed':op})    

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    Customer = customer.objects.get(id=custid)
    Cart = cart.objects.filter(user=user)
    for c in Cart:
        Orderplaced(user=user, customer=Customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orderlist") 


class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists
        return render(request, 'ehome/product-detail.html',{'product':product,'item_already_in_cart':item_already_in_cart})


def shop(request,data=None):
    if data == None:
        Fruits_Vegetables = Product.objects.filter(category='FV')
    elif data == 'Fruits' or data == 'Vegetables':
        Fruits_Vegetables = Product.objects.filter(category='FV').filter(brand=data)
    elif data == 'below':
        Fruits_Vegetables = Product.objects.filter(category='FV').filter(discounted_price__lt=100)
    elif data == 'above':
        Fruits_Vegetables = Product.objects.filter(category='FV').filter(discounted_price__gt=100)
    return render(request, 'ehome/shop.html',{'Fruits_Vegetables':Fruits_Vegetables})

@method_decorator(login_required,name='dispatch')
class ProdileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'ehome/profile.html', {'form':form})

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            cus = customer(user=usr, name=name, phone=phone, email=email, locality=locality, city=city, zipcode=zipcode, state=state)
            cus.save()
            messages.success(request, 'Confratulations! Profile Updated Successfully')
        return render(request, 'ehome/profile.html', {'form':form})



def wishlist(request):
    return render(request, 'ehome/wishlist.html')

def footsubscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')   
        EM =  footnewslatter(email=email)
        EM.save()
    return render(request,'ehome/index.html')

def contctform(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')   
        CF =  contactform(fullname=fullname,phone=phone,email=email,message=message)
        CF.save()
    return render(request,'ehome/contact.html')

class CutomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'ehome/customerregistration.html', {'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! Registered Successfully')
            form.save()
        return render(request,'ehome/customerregistration.html', {'form':form})
   




