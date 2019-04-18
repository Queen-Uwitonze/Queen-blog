from django import forms
from django.core.files import File
from .models import Comments,Like


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','post']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ['user']

class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(label='Email')