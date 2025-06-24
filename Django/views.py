from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def hello_page(request):
    return render(request,"hello_web\\hello.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Name=",form.cleaned_data['name'])
            print("Email=",form.cleaned_data['email'])
            
    else:
        form =ContactForm()
    return render(request,"hello_web\\contact.html",{'form':form})
            