from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect


def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return render(request, 'posts/posts_index.html')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'posts/posts_index.html', context)
