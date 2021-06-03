from django.forms import ModelForm
from .models import survey, Page1, Page2, Page3, Page4, Page5
from django import forms


class SurveyForm(ModelForm):
    class Meta:
        model = survey
        fields = '__all__'


class Page1Form(ModelForm):
    class Meta:
        model = Page1
        exclude = ('name',)
        widgets = {
            'p1q1': forms.RadioSelect(),

        }

class Page2Form(ModelForm):
    class Meta:
        model = Page2
        exclude = ('name',)
        widgets = {
            'p2q1': forms.RadioSelect(),

        }

class Page3Form(ModelForm):
    class Meta:
        model = Page3
        exclude = ('name',)
        widgets = {
            'p3q1': forms.RadioSelect(),

        }

class Page4Form(ModelForm):
    class Meta:
        model = Page4
        exclude = ('name',)
        widgets = {
            'p4q1': forms.RadioSelect(),

        }

class Page5Form(ModelForm):
    class Meta:
        model = Page5
        exclude = ('name',)
        widgets = {
            'p5q1': forms.RadioSelect(),

        }