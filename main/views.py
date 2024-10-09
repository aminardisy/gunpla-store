from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
import datetime
from django.shortcuts import render, redirect
from main.forms import GunplaForm
from main.models import Gunpla
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_main(request):
    
    context = {
        'nama': request.user.username,
        'kelas': 'PBP B',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_gunpla(request):
    form = GunplaForm(request.POST, request.FILES)

    if form.is_valid() and request.method == "POST":
        gunpla = form.save(commit=False)
        gunpla.user = request.user
        gunpla.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_gunpla.html", context)

@csrf_exempt
@require_POST
def add_gunpla_ajax(request):
    user = request.user
    name = request.POST.get("name")
    image = request.POST.get("image")
    price = request.POST.get("price")
    description = request.POST.get("description")
    size_ratio = request.POST.get("size_ratio")
    extensions = request.POST.get("extensions")
    notes = request.POST.get("notes")

    new_Gunpla = Gunpla(name=name, price=price, description=description, size_ratio=size_ratio, extensions=extensions, notes=notes, user=user, image=image)
    new_Gunpla.save()
    
    return HttpResponse(b"CREATED", status=201)
    

def edit_gunpla(request, id):
    gunpla = Gunpla.objects.get(pk = id)

    form = GunplaForm(request.POST or None, instance=gunpla)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_gunpla.html", context)


def delete_gunpla(request, id):
    gunpla = Gunpla.objects.get(pk = id)
    gunpla.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Gunpla.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Gunpla.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Gunpla.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Gunpla.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        messages.error(request, "Invalid username or password. Please try again.")
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
# Create your views here,.
