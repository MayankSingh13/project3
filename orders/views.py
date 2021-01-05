from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        print('Goodbye')
        form = RegisterForm()
    return render(request, 'orders/index.html', {'form': form})
