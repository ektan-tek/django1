from django import forms

from .models import Post

#PostForm - name of the model
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)   #Show only title & text, that need user input
