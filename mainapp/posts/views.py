"""Posts app views configuration"""
from django.shortcuts import render, redirect
from .forms import PostForm, PostComment
from .models import ModelPost, Comment


def posts_page(request):
    """Configuration of posts page"""
    if request.method == "POST":
        comment_form = PostComment(request.POST)
        if comment_form.is_valid():
            comment_form = comment_form.save(commit=False)
            comment_form.name = request.user
            comment_form.save()
            # return render(request, 'posts/posts_index.html')
            comment_form = PostComment
    else:
        comment_form = PostComment()

    list_of_posts = ModelPost.objects.all().values()
    comment = Comment.objects.all().values()
    context = {
        'list_of_posts': list_of_posts,
        'comment_form': comment_form,
        'comment': comment,
    }
    return render(request, 'posts/posts_index.html', context)


def adding_post(request):
    """configuration of page of adding posts"""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            form = PostForm
            return redirect('posts')

    else:
        form = PostForm()

    form_context = {
        'form': form
    }
    return render(request, 'posts/posts_add.html', context=form_context)
