from django.shortcuts import render, get_object_or_404
from .models import Product, Category
 
def product_list(request, category_slug=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
 
    sort = request.GET.get('sort')
    if sort == 'new':
        products = products.order_by('-created_at')
    elif sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    context = {
        "title": "Home page",
        "categories": categories,
        "category": category,
        "products": products
    }
 
    return render(request, "main/product_list.html", context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    product.save()
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    context = {
        "title": product.name,
        "product": product,
        "related_products": related_products
    }
    return render(request, "main/product_detail.html", context)