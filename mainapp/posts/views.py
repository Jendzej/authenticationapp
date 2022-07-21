"""Posts app views configuration"""
import hashlib
import io
import time

from django.http import FileResponse
from django.shortcuts import render, redirect
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            if len(request.FILES) != 0:
                form.image = request.FILES['image']
                print(request.FILES)
            form.save()
            form = PostForm
            return redirect('posts')

    else:
        form = PostForm()
    img_obj = form.instance
    form_context = {
        'form': form,
        'img_obj': img_obj
    }
    return render(request, 'posts/posts_add.html', context=form_context)


def delete_post(request, post_id=None):
    """configuration of deleting posts page"""
    post_to_delete = ModelPost.objects.get(id=post_id)
    if request.method == "POST":
        post_to_delete.delete()
        return redirect('posts')
    if "button_no" in str(request):
        return redirect('posts')
    context = {
        'post_id': post_id,
        'post_to_delete': post_to_delete
    }
    return render(request, 'posts/posts_delete.html', context)


def edit_post(request, post_id=None):
    """configuration of editing posts page"""
    post_to_edit = ModelPost.objects.get(id=post_id)
    if request.method != "POST":
        post_form = PostForm(instance=post_to_edit)

    else:
        post_form = PostForm(instance=post_to_edit, data=request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts')
    context = {
        'post_form': post_form
    }
    return render(request, 'posts/posts_edit.html', context)


def get_pdf(request, post_id=None):
    """Getting pdf view"""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    # lines = [
    #     ""
    # ]
    # for line in lines:
    #     textob.textLine(line)
    post_to_print = ModelPost.objects.get(id=post_id)
    # comments = []
    # for comment in post_to_print.comments.values():
    #     comments.append(comment)
    # lines = [
    #     f"Post Title: {post_to_print.title}",
    #     f"Author: {post_to_print.user}",
    #     f"Post content: {post_to_print.post_content}",
    #     str(comments),
    #     f" ===== "
    # ]
    comments = []
    for comment in Comment.objects.all().values_list('content'):
        # for key, data in comment:
        #     print(key)
        #     comments.append(data)
        comments.append(str(comment).replace("(", "").replace(")", ""))
    textob.textLine(f"Post Title: {post_to_print.title}")
    textob.textLine(f"Author: {post_to_print.user}")
    textob.textLine(f"Post content: {post_to_print.post_content}")
    textob.textLine("Comments:")
    for comm in comments:
        textob.textLine(f"- {comm}")
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    name_post = hashlib.md5(str(time.time).encode())
    return FileResponse(buf, as_attachment=True, filename=f'{name_post.hexdigest()}')
