from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import HttpResponse,HttpResponseRedirect,Http404
from django.contrib import messages
from .models import postspage
from.forms import postform
# from django.db.models import Q

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render

def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated():
        raise Http404

    form=postform(request.POST or None,request.FILES or None)
    if(form.is_valid()):
        instance=form.save(commit=False)
        instance.user =request.user
        instance.save()
        messages.success(request,"Successfully Uploaded")
        return HttpResponseRedirect(instance.get_absolute_url())
    context ={
        "form":form,
    }
    return render(request,'create.html',context)

def posts_detail(request,id):
    instance = get_object_or_404(postspage,id=id)
    string = quote_plus(instance.title)
    context ={
        "string": string,
        "instance": instance,
    }
    print("**"+string+"--")
    return render(request,'detail.html',context)
    # return render(request,'detail.html',{'list': instance})

def posts_list(request):
    queryset_list = postspage.objects.all().order_by("-timestamp")
    query=request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(title__icontains=query)

    paginator = Paginator(queryset_list , 5)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request,'list.html',{'list': queryset})

def posts_update(request,id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(postspage,id=id)
    form=postform(request.POST or None,request.FILES or None,instance=instance)
    if(form.is_valid()):
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully Edited")
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context ={
        "title": instance.title,
        "instance":instance,
        "form":form,
    }
    return render(request,'create.html',context)

def posts_delete(request,id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(postspage,id=id)
    instance.delete()
    messages.success(request,"Successfully deleted")
    return redirect("list")