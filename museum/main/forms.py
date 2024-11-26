from .models import Exhibition, Museum_Room
from django.forms import ModelForm, TextInput, DateInput
from django.forms.widgets import Select


class ExhibitionForm(ModelForm):
    class Meta:
        model = Exhibition
        fields = ['name', 'start_date', 'end_date', 'country', 'city', 'venue', 'responsible_person', 'museum']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }),
            'start_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Начальная дата'
            }),
            'end_date': DateInput(attrs={
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


class MuseumRoomForm(ModelForm):
    class Meta:
        model = Museum_Room
        fields = ['room_number', 'description', 'museum']

        widgets = {
            'room_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер',
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
            'museum': Select(attrs={
                'class': 'form-control',
            })
        }
