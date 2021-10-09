from django import forms
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _



class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, label = 'Comentario', widget=forms.Textarea(attrs={
        'class': 'col-md-9',
        'style': 'background-color:#121212' 
    }))

    name = forms.CharField(required=True, label = 'Nombre', widget=forms.Textarea(attrs={
        'rows': 1,
        'style': 'background-color:#121212' 
    }))
    class Meta:
        model = Comment
        fields = ('content','name',)
        
