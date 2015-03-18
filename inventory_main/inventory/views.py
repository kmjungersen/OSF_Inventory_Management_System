from django.shortcuts import render, get_object_or_404

from inventory.models import Product

# Create your views here.

def index(request):
    latest_product_list = Product.objects.all()[:5]

    return render(request, 'inventory/products.html', {'products': latest_product_list})

def add_product(request, question_id):

    p = Product(name=request.POST['name'])

    p.save()

