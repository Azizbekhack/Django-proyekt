from django.contrib import admin
from .models import Contact,Category,Blog,Portfolio,PortfolioCategory

# Register your models here.

admin.site.register((Contact,Category,Blog,PortfolioCategory,Portfolio)) 
