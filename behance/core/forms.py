from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Work, Comment


class Workform(ModelForm):
    class Meta:
        model = Work
        fields = '__all__'


class Commentform(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        labels = {
            'text': 'Add your comment'
        }