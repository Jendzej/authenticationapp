from django.forms import ModelForm, TextInput
from .models import ModelPost


class PostForm(ModelForm):
    class Meta:
        model = ModelPost
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={'class': "post_add", 'placeholder': 'Title of your post'}),
            'content': TextInput(attrs={'class': "post_add", 'placeholder': 'Content of your post'})
        }
