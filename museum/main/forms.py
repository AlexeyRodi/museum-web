from .models import Exhibition
from django.forms import ModelForm, TextInput, DateTimeInput
from django.forms.widgets import Select

class ExhibitionForm(ModelForm):
    class Meta:
        model = Exhibition
        fields = ['name','start_date','end_date','country','city','venue','responsible_person', 'museum']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'start_date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Начальная дата'
            }),
            'end_date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Конечная дата'
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            'venue': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место проведения'
            }),
            'responsible_person': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ответсвенное лицо'
            }),

            'museum': Select(attrs={
                'class': 'form-control',
            }),


        }