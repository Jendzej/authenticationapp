from django.forms import ModelForm, TextInput, Textarea
from .models import ModelPost, Comment


class PostForm(ModelForm):
    class Meta:
        model = ModelPost
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={'class': "post_add_t", 'placeholder': 'Title of your post'}),
            'content': Textarea(attrs={'class': "post_add_c", 'placeholder': 'Content of your post'})
        }


class PostComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'post']
        widgets = {
            'content': TextInput(attrs={'class': "comment_post", 'placeholder': 'Write a comment...'}),

        }
