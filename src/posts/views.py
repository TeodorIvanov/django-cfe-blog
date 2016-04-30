from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
# Create your views here.
from .models import Post
#function based views vs class based views
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form,
        }
    return render(request, "post_form.html", context)
    #return render(request, "post_create.html", context)

def post_detail(request, id=None):  #retrieve/read
    #instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_list(request):  #list items
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
        }
    return render(request, "index.html", context)
    #return HttpResponse("<h1>list</h1>")

def post_list_newest(request):  #list items
    queryset = Post.objects.all()[::-1]
    context = {
        "object_list": queryset,
        "title": "List"
        }
    return render(request, "index_newest.html", context)

def post_update(request):
    return HttpResponse("<h1>update</h1>")

def post_delete(request):
    return HttpResponse("<h1>delete</h1>")
