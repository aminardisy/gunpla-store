from django.urls import path
from main.views import register, login_user, logout_user
from main.views import show_main, create_gunpla, edit_gunpla, delete_gunpla
from main.views import show_xml, show_json, show_xml_by_id, show_json_by_id
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('create-gunpla', create_gunpla, name='create_gunpla'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-gunpla/<uuid:id>', edit_gunpla, name='edit_gunpla'),
    path('delete/<uuid:id>', delete_gunpla, name='delete_gunpla'), 
]