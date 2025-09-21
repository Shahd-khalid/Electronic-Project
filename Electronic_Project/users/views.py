from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # تشفير كلمة السر
            user.save()
            return redirect('login')  # لاحقًا يمكن صفحة تسجيل الدخول أو قائمة المستخدمين
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # تحقق إذا كان لديه متجر مرتبط → تحويله مباشرة للوحة التحكم
                if hasattr(user, 'shop'):
                    return redirect('home')
                else:
                    return redirect('home')  # المستخدم عادي لا يملك متجر
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
