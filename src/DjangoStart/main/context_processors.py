from main.cart import Cart

def cart(request):
    if Cart is None:
        raise ImportError("Не вдалося імпортувати Cart")
    return {'cart': Cart(request)}