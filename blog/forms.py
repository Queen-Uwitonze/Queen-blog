from django import forms
from django.core.files import File
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user']

# class VotesForm(forms.ModelForm):
#     class Meta:
#         model = Votes
#         exclude = ['user']