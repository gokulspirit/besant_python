from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def hello_page(request):
    return render(request,"hello_web\\hello.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')