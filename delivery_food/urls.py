"""delivery_food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurants import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('restaurant/<int:rest_id>', views.restaurant, name='restaurant'),
    path('search', views.search, name='search'),
    path('add_food/<int:food_id>', views.add_food, name='add_food'),
    path('del_food/<int:food_id>', views.del_food, name='del_food'),
    path('cart', views.cart, name='cart'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)