from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect

from .models import Blogpost
from .forms import BlogPostForms, BlogPostModelForm
#def blog_post_detail(request,slug):
   # queryset = Blogpost.objects.filter(slug=slug)
    #obj = get_object_or_404(Blogpost,slug=slug)
   # if queryset.count() == 0:
       # raise Http404
    #obj = queryset.first()
    #context = {"object":obj}
    #return render(request,'blog_post_detail.html',context)


#CRUD
# CREATE-RETRIEVE(list)-UPDATE-DELETE

def blog_post_list_view(request): 
    #list objects
    #could be search
    qs = Blogpost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = Blogpost.objects.filter(user=request.user)
        qs = (qs |my_qs ).distinct()
    context = {"object_list":qs}
    return render(request,"blog/list_view.html",context)

#@login_required
@staff_member_required 
def blog_post_create_view(request):
    form =  BlogPostModelForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user 
        obj.save()
        form =  BlogPostModelForm()
    context = {"form":form,
        "title":"Blog Page"}
     #create objects
     #? use a form
    return render(request,'form.html',context)
@staff_member_required 
def blog_post_detail_view(request,slug): #retrieve
    obj = get_object_or_404(Blogpost,slug=slug)
    context = {"object":obj}
    return render(request,'blog/detail_view.html',context)

@staff_member_required 
def blog_post_update_view(request,slug):
    obj = get_object_or_404(Blogpost,slug=slug)
    form =  BlogPostModelForm(request.POST or None,instance=obj)
    if form.is_valid():
         form.save()
    
    context = {"form":form,"title":f"UPDATE{obj.title}"}
    return render(request,'form.html',context)

@staff_member_required 
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(Blogpost,slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object":obj}
    return render(request,'blog/delete_view.html',context)
    
