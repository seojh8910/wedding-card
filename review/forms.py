from django import forms
from django.forms import ModelForm

from review.models import Review


class ReviewCreationForm(ModelForm):
    content = forms.CharField(required=True)
    image = forms.ImageField(required=True)

    class Meta:
        model = Review
        fields = ['content', 'image']
