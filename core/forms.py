from random import choice

from django import forms
from  .models import Calc


class CalcForm(forms.ModelForm):
    options = [
        ('Add' , '+'),
        ("Subtract" , '-'),
        ("divide" , '%') ,
        ("Multiply" , '*')
    ]

    operation = forms.ChoiceField(choices = options)

    class Meta :
        model = Calc
        fields = ['first_number' , 'second_number' , 'operation']
        widgets = {
            'first_number': forms.NumberInput(attrs={'placeholder': 'Enter first number'}),
            'second_number': forms.NumberInput(attrs={'placeholder': 'Enter second number'}),
        }

