from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Driver
from django.urls import reverse
from .models import Driver
from .forms import DriverForm
from django.contrib.auth import login,  logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import LoginForm, RegistrationForm
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.


def homePage(request):
    # Search Functionality 
    if 'q' in request.GET:
        q = request.GET['q']
        drivers = Driver.objects.filter(firstName__icontains=q)
    else:
        drivers = Driver.objects.all()

    # Pagination
    paginator = Paginator(drivers, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'drivers' : drivers, 'page_obj' : page_obj}
    return render(request, 'system/home.html', context)


def driver(request, pk):
    driver = Driver.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home'))


def addDriver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DriverForm()
    context = {'form' : form}
    return render(request, 'system/add.html', context)


def editDriver(request, id):
    if request.method == 'POST':
        driver = Driver.objects.get(pk=id)
        form = DriverForm(request.POST, request.FILES, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        driver = Driver.objects.get(pk=id)
        form = DriverForm(instance=driver)
    context = {'form' : form, 'driver' : driver}
    return render(request, 'system/edit.html', context)

def deleteDriver(request, id):
    if request.method == 'POST':
        driver = Driver.objects.get(pk=id)
        driver.delete()
        return redirect('home')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Admin Registration Successful.....')
            return redirect('home')
        else:
            messages.error(request, 'Registration Unsuccessful,Please Enter valid credentials and Try again later')
    else:
        form = RegistrationForm()
    context = {'form' : form}
    return render(request, 'system/register.html', context)



def login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now Logged in as {username}')
                return redirect('home')
            else:
                messages.error(request, 'Invalid Username or Password')
        else:
            messages.error(request, 'Invalid Username or Password')
    else:
        form = LoginForm()
    context = {'form' : form}
    return render(request, 'system/login.html', context)

def logout(request):
    logout(request)
    messages.info(request, 'You have Successfully Logged Out')
    return redirect('login')


def profile(request, id):
    driver = Driver.objects.get(pk=id)
    context = {'driver' : driver}
    return render(request, 'system/profile.html', context)



