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
        fields = '__all__'
        widgets = {
            'p1q1': forms.RadioSelect(),

        }

class Page2Form(ModelForm):
    class Meta:
        model = Page2
        fields = '__all__'
        widgets = {
            'p2q1': forms.RadioSelect(),

        }

class Page3Form(ModelForm):
    class Meta:
        model = Page3
        fields = '__all__'
        widgets = {
            'p3q1': forms.RadioSelect(),

        }

class Page4Form(ModelForm):
    class Meta:
        model = Page4
        fields = '__all__'
        widgets = {
            'p4q1': forms.RadioSelect(),

        }

class Page5Form(ModelForm):
    class Meta:
        model = Page5
        fields = '__all__'
        widgets = {
            'p5q1': forms.RadioSelect(),

        }