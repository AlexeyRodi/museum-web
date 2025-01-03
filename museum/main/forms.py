from .models import Exhibition, MuseumRoom, Exhibit
from django.forms import ModelForm, TextInput, DateInput
from django.forms.widgets import Select, ClearableFileInput


class ExhibitionForm(ModelForm):
    class Meta:
        model = Exhibition
        fields = ['name', 'start_date', 'end_date', 'country', 'city', 'venue', 'responsible_person', 'museum', 'image']

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

            'image': ClearableFileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*',
            }),

        }


class MuseumRoomForm(ModelForm):
    class Meta:
        model = MuseumRoom
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


class ExhibitForm(ModelForm):
    class Meta:
        model = Exhibit
        fields = ['name', 'description', 'creation_year', 'creator', 'room']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),

            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),

            'creation_year': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата создания'
            }),

            'creator': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Создатель'
            }),

            'room': Select(attrs={
                'class': 'form-control'
            })
        }


class ExhibitMuseumForm(ModelForm):
    class Meta:
        model = Exhibit
        fields = ['name', 'description', 'creation_year', 'creator']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),

            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),

            'creation_year': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата создания'
            }),

            'creator': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Создатель'
            }),
        }
