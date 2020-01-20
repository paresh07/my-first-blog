from django import forms

from .models import Post

class PostForm(forms.ModelForm):    #forms.ModelForm is responsible to tell Django that this form is a ModelForm

    class Meta:     #class Meta, where we tell Django which model should be used to create this form (model = Post).
        model = Post
        fields = ('title', 'text',)     #field we want to edit