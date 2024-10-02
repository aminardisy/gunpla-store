from django.forms import ModelForm
from main.models import Gunpla

class GunplaForm(ModelForm):
    class Meta:
        model = Gunpla
        fields = ["name", "image", "price", "description", "size_ratio", "extensions", "notes"]