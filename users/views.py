from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request, "회원가입을 환영합니다")
            signed_user.send_email()
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, 'users/signup_form.html',{
        'form': form,
    })
