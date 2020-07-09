from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from blog.models import Blogpost


def home_page(request):
    my_title= "hello home"
    qs = Blogpost.objects.all()[:5]
    context = {"title":"Welcome to Try Django","blog_list":qs}
    return render(request,"home.html",context)

def about_page(request):
    return render(request,"about.html",{"title":"About Us"})  

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        obj = Blog
    print(form.cleaned_data)
    form = ContactForm()
    context= {"form":form,
              "title":"Contact Us"}

    return render(request,"form.html",context)    
