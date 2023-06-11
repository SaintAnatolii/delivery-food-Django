from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Restaurant, Product, Cart
from user.models import User
from user.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth, messages

def home(request):
    context = {
        'restaurants':Restaurant.objects.all()
    }
    return render(request, 'index.html', context)

def restaurant(request, rest_id):
    context = {
        'products' : Product.objects.filter(restaurant=rest_id),
        'restaurant' : Restaurant.objects.get(id=rest_id)
    }

    return render(request, 'restaurant.html', context)

def search(request):
    if request.method == 'POST':
        title = request.POST.get('searching')
        products = Product.objects.filter(name__iregex=title)
        restaurants = Restaurant.objects.filter(name__iregex=title)

        context = {
            'products':products,
            'restaurants':restaurants
        }
    
    return render(request, 'search.html', context)

def add_food(request, food_id):
    product = Product.objects.get(id=food_id)
    cart = Cart.objects.filter(user=request.user, product=product)
    if not cart.exists():
        Cart.objects.create(user=request.user, product=product, amount=1)
    else:
        cart = cart.first()
        cart.amount += 1
        cart.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def del_food(request, food_id):
    product = Cart.objects.get(product_id=food_id)
    product.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def cart(request):
    cart = Cart.objects.filter(user=request.user)
    total_sum = 0
    for item in cart:
        total_sum += item.sum()
    context = {
        'cart':cart,
        'total_sum' : total_sum
    }
    return render(request, 'cart.html', context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()

    form = UserLoginForm()
    return render(request, 'login.html', {'form':form})


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'registration.html', context)