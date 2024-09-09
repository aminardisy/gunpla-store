from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'MG GUNDAM F90',
        'price': 'RP 420.000,00 ',
        'size_ratio': '1/100',
        'extensions': 'stand base',
        'notes':'*The product in the image is a prototype still in its developmental stage. The product is also painted. The actual product may appear differently from the image. *Please note that in some cases bubbles may enter the clear parts during manufacturing process.'
    }

    return render(request, "main.html", context)
# Create your views here.
