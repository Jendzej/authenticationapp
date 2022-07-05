from django.shortcuts import render
from .forms import PostForm


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
