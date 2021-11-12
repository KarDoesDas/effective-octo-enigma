from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class Home(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

HomeView = Home.as_view()

class Registration(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST)
        # Data verify


        # user create in database

        # user login

        # if successfull login redirect to home page (to upload pics)

        # if fail return error messages and reload registration page

        
        return render(request, self.template_name)

RegistrationView = Registration.as_view()