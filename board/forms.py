from django import forms
from django.forms import ModelForm

from board.models import Board, Comment


class BoardCreationForm(ModelForm):
    title = forms.CharField(max_length=150, required=True,
                            widget=forms.TextInput(
                                attrs={'style': 'width: 82%; margin-right: 3%; padding: 10px;',
                                       'placeholder': '제목을 입력하세요'}))
    content = forms.CharField(required=True,
        widget=forms.Textarea(
            attrs={'class': 'editable text-left',
                    'style': 'width: 82%; margin-right: 3%; height: 17rem; padding: 10px;',
                    'placeholder': '내용을 작성하세요'}))
    is_secret = forms.BooleanField(initial=True, required=False)

    def __init__(self, *args, user=None, **kwargs):
        super(BoardCreationForm, self).__init__(*args, **kwargs)
        if user and user.is_staff:
            self.fields['is_notice'] = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = Board
        fields = ['title', 'content', 'is_secret', 'content', 'is_notice']


class CommentCreationForm(ModelForm):
    content = forms.CharField(required=True, max_length=100)

    class Meta:
        model = Comment
        fields = ['content']

