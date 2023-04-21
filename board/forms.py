from django import forms
from django.http import request

from .models import Board, BoardImage


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'contents', 'image')


class ImageForm(forms.ModelForm):
    class Meta:
        model = BoardImage
        fields = ('image_title',  'image')

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')