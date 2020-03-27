from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserOurRegistration(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserOurRegistration, self).__init__(*args, **kwargs)
        del self.fields['password2']

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'email']  # 'choise']


class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None


    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']



class ProfileEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileEdit, self).__init__(*args, **kwargs)
        # self.fields['img'].label = 'Изображение профиля'
        # self.fields['gender'].label = 'Выбeрите пол'
        # self.fields['agree'].label = 'Соглашение про отправку уведомлений на почту'


    class Meta:
        model = User

        fields = ['username', 'email']# , 'email'] # , 'gender', 'agree']
