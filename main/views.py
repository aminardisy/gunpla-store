from django.shortcuts import render

def show_main(request):
    context = {
        'nama:': 'Ardi Syahputra Amin',
        'kelas': 'PBP B',
        'name' : 'MG GUNDAM F90',
        'price': '420.000',
        'description' : 'Technology & Combat Characteristics The Gundam F90 is a prototype unit developed by the Strategic Naval Research Institute under the “Formula Project”, a plan to create small mobile suits. Standing at only 14.8 meters compared to the 18 meters tall RX-78-2 Gundam, the Gundam F90’s downsizing was achieved through the use of micro-honeycomb structure obtained from Yashima Heavy Industries, enabling its armor and movable frame to be made lighter. It also has a downsized reactor, but its output is 1.5 times that of existing mobile suits. With a total of 51 attitude control thrusters placed throughout its body, the Gundam F90 is also highly mobile and maneuverable. A total of three Gundam F90 units were built and are known as Unit 1 to Unit 3. The Gundam F90’s most prominent feature is its adaptation of the Mission Packs. These dedicated optional equipment can be attached across the 11 hardpoints placed throughout the Gundam F90’s body, allowing the mobile suit to take on a variety of missions. They can also be exchanged when needed, granting the Gundam F90 extremely high versatility. To control the Mission Packs, pseudo-personality computers were installed. Unit 1 has the Type-A.R., while Unit 2 has the Type-C.A. The Gundam F90’s standard armament consist of two head vulcans, a beam rifle, two beam sabers, and a shield.',
        'size_ratio': '1/100',
        'extensions': 'stand base',
        'notes':'*The product in the image is a prototype still in its developmental stage. The product is also painted. The actual product may appear differently from the image. *Please note that in some cases bubbles may enter the clear parts during manufacturing process.'
    }

    return render(request, "main.html", context)
# Create your views here.
