from django.shortcuts import render
from .models import Category
def menu_home(request):
    categories = Category.objects.filter(active=True).prefetch_related("products")
    return render(request, "menu/home.html", {"categories": categories})
