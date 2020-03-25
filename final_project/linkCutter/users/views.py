from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserOurRegistration, UserUpdateForm, ProfileEdit
from django.contrib.auth.decorators import login_required


def register(request, **kwargs):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        print(form)
        if form.is_valid():
            form.save(**kwargs)
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Аккаунт {username} был успешно создан!Введите имя пользователя и пароль для авторизации.')
            return redirect('user')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Страница регистрации пользователя'})


@login_required
def showprofile(request, **kwargs):
    if request.method == "POST":
        # edit_profile = ProfileEdit(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid():  # and edit_profile.is_valid():
            # edit_profile.save(**kwargs)
            update_user.save(**kwargs)
            messages.success(request, f'Аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        # edit_profile = ProfileEdit(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)

    data = {

        # 'edit_profile': edit_profile,
        'update_user': update_user,
        'required': '',
    }


    return render(request, 'users/profile.html', data)
