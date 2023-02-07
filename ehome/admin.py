from django.contrib import admin
from .models import *

@admin.register(footnewslatter)
class  footsubscribe(admin.ModelAdmin):
    list_display = ('id', 'email')

@admin.register(contactform)
class  contact_form(admin.ModelAdmin):
    search_fields = [
        'fullname',
        'phone',
        'email',
    ]
    list_pr_page = 25
    list_display = ('id', 'fullname','phone','email')



@admin.register(customer)
class customerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name', 'locality', 'city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = [
        'product_title',
        'selling_price',
        'brand',
        'category',
    ]
    list_display = ['id','product_title','selling_price','discounted_price','product_avail','brand','category','product_img']


@admin.register(cart)
class cartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product', 'quantity']

@admin.register(Orderplaced)
class OrderplacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer', 'product','quantity','ordered_date','status']




