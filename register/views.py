# from http.cookiejar import lwp_cookie_str
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first
from django.views import View
from .models import User
from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect

from django.views.generic import TemplateView
from.forms import UserForm
# Create your views here.

class RegisterView(TemplateView):
    template_name = 'register.html'
    def get_user_data(request):
        form = UserForm(request.GET or None)

        first_name =  request.GET.get('first_name')

        last_name =request.GET.get('last_name')

        email = request.GET.get('email')

        role  = request.GET.get('role')

        is_active = request.GET.get('is_active')


        username =  request.GET.get('username')
        password = request.GET.get('password')

        context = {
            'first':first_name,
            'last_name':last_name,
            'email':email,
            'role':role,
            'username':username,
            'password':password,
            'is_active':is_active,

        }
        return render(request,'register.html', context)

    def post(self,request,*args,**kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])

            form.save()
            return redirect('http://127.0.0.1:8000/blog/')

        return HttpResponse('register error'+str(form.errors))


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')


        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse('invalid email or password')

        if user.check_password(password):
            return redirect('http://127.0.0.1:8000/blog/')

        else:
            return HttpResponse('invalid email or password')