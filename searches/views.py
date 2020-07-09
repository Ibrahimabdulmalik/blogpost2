from django.shortcuts import render
from blog.models import Blogpost
from .models import SearcheQuery


# Create your views here.
def search_view(request):

    query = request.GET.get('q',None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query":query}    
    if query is not None:    
     SearcheQuery.objects.create(user=user,query=query)  
     blog_list = Blogpost.objects.search(query=query)  
    context['blog_list'] = blog_list
    return render(request,'searches/view.html',context)