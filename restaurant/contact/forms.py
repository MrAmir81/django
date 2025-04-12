from django import forms #type:ignore
from .models import Contact

class ContatForm(forms.ModelForm):
     class Meta:           
        model = Contact
        fields = "__all__"