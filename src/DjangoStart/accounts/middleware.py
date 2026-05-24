from django.shortcuts import redirect
 
class AdminAccessRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
 
    def __call__(self, request):
        # Якщо користувач намагається зайти в адмінку
        if request.path.startswith('/admin/'):
            user = request.user
            # Якщо користувач не увійшов, або не є адміністратором (staff)
            if not user.is_authenticated or not user.is_staff:
                return redirect('main:product_list')
        return self.get_response(request)