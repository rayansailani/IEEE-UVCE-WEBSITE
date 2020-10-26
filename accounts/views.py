from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from accounts.forms import RegistrationForm, AccountAuthenticationForm
from accounts.models import Account
# Create your views here.


def register_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('articles:s_dashboard')
        else:
            context['registration_form'] = form
    else:  # GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)


# def login_view(request):
#     context = {}
#     sig_heads = Account.objects.all().filter(is_sig_head=True)
#     # sig_heads = Account.objects.all('is_sig_head')
#     user = request.user
#     if user.is_authenticated:
#         return redirect('articles:list')
#     if request.POST:
#         form = AccountAuthenticationForm(request.POST)
#         if form.is_valid:
#             email = request.POST['email']
#             password = request.POST['password']
#             user = authenticate(email='email', password='password')
#             if user:
#                 login(request, user)
#                 if 'next' in request.POST:
#                     return redirect(request.POST.get('next'))
#                 if user in sig_heads:
#                     return redirect('articles:list')
#                 else:
#                     return redirect('/')
#     else:
#         form = AccountAuthenticationForm()
#     context['login_form'] = form
#     return render(request, 'accounts/login.html', context)


def login_view(request):
    context = {}
    sig_heads = Account.objects.all().filter(is_sig_head=True)
    user = request.user
    if user.is_authenticated:
        return redirect('home_page')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():

            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                if user.is_sig_head:
                    return redirect('articles:dashboard')
                else:
                    return redirect('articles:s_dashboard')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'accounts/login.html', context)


# def login_view(request):
#     if request.method == 'POST':
#         form = AccountAuthenticationForm(data=request.POST)
#         if form.is_valid():
#             # log in the user
#             user = form.get_user()
#             login(request, user)
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect('articles:list')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
# # url -> view -> html
