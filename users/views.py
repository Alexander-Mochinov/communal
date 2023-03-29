from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate

from users.models import User


def registration(request):
    if request.method == "POST":
        email = request.POST.get("email")
        personal_account = request.POST.get("personal_account")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Такой пользователь уже существует !')
            return redirect('/account/login/')

        user = User(email=email, personal_account=personal_account)
        user.set_password(password)
        user.save()

        return redirect('/')

    return HttpResponse("Method Allowed")


def personal_account(request):

    return render(request, 'account/personal_page.html', {})


def profile_form(request):

    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':

        data = {
            "second_name": request.POST.get("second_name"),
            "first_name": request.POST.get("first_name"),
            "patronymic": request.POST.get("patronymic"),
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
        }

        for key, value in data.items():
            setattr(user, key, value)

        user.save()


    context = {
        "user": user,
    }
    return render(request, "account/profile-form.html", context)
