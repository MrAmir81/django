from django.shortcuts import render , get_object_or_404 # type: ignore
from .models import Blog , Tag , Category , Comments
from .forms import CommentForm
from django.core.paginator import Paginator # type: ignore

def blog_list(request):
    blogs = Blog.objects.all()

    paginator = Paginator(blogs, 3)
    page_number = request.GET.get("page")
    blog_list = paginator.get_page(page_number)
    context = {
        "blog_list":blog_list
    }
    return render(request,"blog/blog_list.html",context)

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all()
    recents = Blog.objects.all().order_by("created_at")[:2]
    categories = Category.objects.all()
    comments = Comments.objects.all().filter(blog=blog)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            new_comment = Comments(blog=blog,name=name,email=email,message=message)
            new_comment.save()

    context = {
        "blog":blog,
        "tags":tags,
        "recents":recents,
        "categories":categories,
        "comments":comments,
        }
    return render(request,"blog/blog_detail.html",context)

def blog_tag(request,tag):
    blogs = Blog.objects.filter(tags__slug=tag)
    
    context = {
        "blogs":blogs
    }
    return render(request,"blog/blog_list.html",context)

def blog_category(request,category):
    blogs = Blog.objects.filter(category__slug=category)
    
    context = {
        "blogs":blogs
    }
    return render(request,"blog/blog_list.html",context)

def search(request):
    if request.method == "GET":
        x = request.GET.get("search")
    blog_list = Blog.objects.filter(title__icontains=x)
    return render(request,"blog/blog_list.html",{"blog_list":blog_list})
