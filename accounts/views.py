from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username, password)
    else:
        form = SignUpForm()

    context = {"form": form}
    return render(request, "registration/signup.html", context) 
