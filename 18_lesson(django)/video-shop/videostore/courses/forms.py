from django import forms
from .models import Course


class CreateCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateCourseForm, self).__init__(*args, **kwargs)
        self.fields['slug'].label = 'Название URL'
        self.fields['title'].label = 'Название курса'
        self.fields['description'].label = 'Описание курса'
        self.fields['img'].label = 'Изображение профиля'

    class Meta:
        model = Course
        fields = ['slug', 'title', 'description', 'img']
