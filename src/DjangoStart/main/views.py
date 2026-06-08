from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Category
from .forms import ContactForm
from .cart import Cart
 
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


def contact_view(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Отримуємо валідовані дані з форми
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_text = form.cleaned_data['message']
            
            # Тут за потреби можна реалізувати надсилання листа на email адміна за допомогою send_mail()
            # Наприклад:
            # from django.core.mail import send_mail
            # send_mail(f"Тема: {subject}", f"Від: {name} ({email})\n\n{message_text}", email, ['admin@blog.com'])

            # Додаємо сповіщення про успіх у сесію користувача
            messages.success(request, "Дякуємо! Ваше повідомлення успішно надіслано. Ми зв'яжемося з вами найближчим часом.")
            
            # Перенаправляємо користувача назад на порожню форму
            return redirect('main:contact')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {
        'form': form,
        'categories': categories,
        'title': 'Контакти'
    })

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('main:product_list')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('main:product_list')  

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'main/cart_detail.html', {'cart': cart})