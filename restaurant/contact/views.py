from django.shortcuts import render #type:ignore
from .forms import ContatForm

def contact(request):
   contact = ContatForm()
   if request.method == "POST":
        contact  = ContatForm(request.POST)
        if contact .is_valid():
            contact .save()
   else:
       contact  = ContatForm()

   context = {
        "contact":contact
    }
   return render (request,"contact.html",context)