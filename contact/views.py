from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse

# Create your views here.

def send_message(request):
    pass
    # if request.method=='POST':
    #     form = JobForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         myform = form.save(commit=False)
    #         myform.owner = request.user
    #         myform.save()

    #         return redirect(reverse('jobs:job_list'))
    # else:
    #     form = JobForm()

    # context = {"form": form}

    # return render(request, "contact/send_message.html", context)




