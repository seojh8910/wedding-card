from django import forms
from django.forms import ModelForm

from board.models import Board, Comment


class BoardCreationForm(ModelForm):
    title = forms.CharField(max_length=150, required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'},),
                              required=True)
    is_secret = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Board
        fields = ['title', 'content', 'is_secret', 'content']


class CommentCreationForm(ModelForm):
    content = forms.CharField(required=True, max_length=100)

    class Meta:
        model = Comment
        fields = ['content']

