from django.urls import reverse
from django.shortcuts import redirect

class AuthenticateMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:

            paths_to_direct = [reverse('myapp:login'), reverse('myapp:register')]

            if request.path in paths_to_direct:
                return redirect(reverse('myapp:dashboard'))

        response = self.get_response(request)
        return response

class RegisterAuthenticated:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        restricted_path = reverse('myapp:dashboard')

        if not request.user.is_authenticated:

            if request.path == restricted_path:

                return redirect(reverse('myapp:login'))

        response = self.get_response(request)
        return response