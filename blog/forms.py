from django import forms
from django.core.files import File
from .models import Comments,Like

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ['user']

# class VotesForm(forms.ModelForm):
#     class Meta:
#         model = Votes
#         exclude = ['user']