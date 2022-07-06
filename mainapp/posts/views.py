from django.shortcuts import render
from .forms import PostForm
from django.http import HttpResponse
from .models import ModelPost
from django.template import loader


def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return render(request, 'posts/posts_index.html')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'posts/posts_index.html', context)


def posts(request):
    list_of_posts = ModelPost.objects.all().values()
    context = {'list_of_posts': list_of_posts}
    return render(request, 'posts/posts_index.html', context)
