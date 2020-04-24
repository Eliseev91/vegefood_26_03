from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .settings.base import *
from django.core.paginator import Paginator

from .models import *

# Create your views here.

class IndexView(View):

    def get(self, request):
    
        for k, v in request.COOKIES.items():
            print(k, v)
    
        return render(request, 'shop/index.html', {'phone_number': PHONE_NUMBER})

class ShopView(View):

    def get(self, request, page_id=1):    
    
        products_list = [{'name':       'Bell Pepper',
                     'image':      'shop/images/product-1.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'}, 
                    {'name':       'Strawberry',
                     'image':      'shop/images/product-2.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Green Beans',
                     'image':      'shop/images/product-3.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Purple Cabbage',
                     'image':      'shop/images/product-4.jpg',
                     'price':      '$120.00'},
                    {'name':       'Tomatoe',
                     'image':      'shop/images/product-5.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'},   
                    {'name':       'Brocolli',
                     'image':      'shop/images/product-6.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Carrots',
                     'image':      'shop/images/product-7.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Fruit Juice',
                     'image':      'shop/images/product-8.jpg',
                     'price':      '$120.00'},     
                    {'name':       'Onion',
                     'image':      'shop/images/product-9.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'},    
                    {'name':       'Apple',
                     'image':      'shop/images/product-10.jpg',
                     'price':      '$120.00'},   
                    {'name':       'Garlic',
                     'image':      'shop/images/product-11.jpg',
                     'price':      '$120.00'},     
                    {'name':       'Chilli',
                     'image':      'shop/images/product-12.jpg',
                     'price':      '$120.00'}]

        # for product in products_list:
        #     p = Shop(name=product['name'], image=product['image'], price=int(product['price'][1:-3]), price_sale=0)
        #     if 'discount' in product:
        #         p.discount = int(product['discount'][:-1])
        #         p.price_sale = int(product['price_sale'][1:-3])
        #     p.save()

        paginator = Paginator(products_list, 12)
        
        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('shop'))
            
        return render(request, 'shop/shop.html', {'products': products, 'phone_number': PHONE_NUMBER})

class ContactView(View):

    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        return render(request, 'shop/contact.html', {'phone_number': PHONE_NUMBER})

class BlogView(View):

    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        blogs = [

            {'image':'shop/images/image_1.jpg',
             'date': 'July 20, 2019',
             'author': 'admin',
             'count_messages': 3,
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'main_text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'
             },

            {'image': 'shop/images/image_2.jpg',
             'date': 'July 20, 2019',
             'author': 'admin',
             'count_messages': 3,
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'main_text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'
             },

            {'image': 'shop/images/image_3.jpg',
             'date': 'July 20, 2019',
             'author': 'admin',
             'count_messages': 3,
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'main_text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'
             },

            {'image': 'shop/images/image_4.jpg',
             'date': 'July 20, 2019',
             'author': 'admin',
             'count_messages': 3,
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'main_text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'
             },

            {'image': 'shop/images/image_5.jpg',
             'date': 'July 20, 2019',
             'author': 'admin',
             'count_messages': 3,
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'main_text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'
             }
        ]

        blogs = []

        for object in Blogs.objects.all():
            d = dict(image=object.image,
                     date=object.data,
                     author=object.author,
                     count_messages=object.count_messages,
                     title=object.title,
                     main_text=object.main_text
                     )
            blogs.append(d)


        return render(request, 'shop/blog.html', {'blogs': blogs})


class CartView(View):

    def get(self, request):
        for k, v in request.COOKIES.items():
            print(k, v)

        return render(request, 'shop/cart.html', {'phone_number': PHONE_NUMBER})
        
        
        
        

        
        
        
        
        
        