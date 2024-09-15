from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import GunplaForm
from main.models import Gunpla

def show_main(request):
    gunplas = Gunpla.objects.all()

    context = {
        'nama': 'Ardi Syahputra Amin',
        'kelas': 'PBP B',
        'gunpla': gunplas
    }

    return render(request, "main.html", context)

def create_gunpla(request):
    form = GunplaForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_gunpla.html", context)

def show_xml(request):
    data = Gunpla.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Gunpla.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Gunpla.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Gunpla.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
# Create your views here,.
