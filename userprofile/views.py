from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect


from userprofile.forms import LoginForm, RegisterForm, ProfileForm
from userprofile.models import UserProfile as User
from django.contrib.auth import get_user_model

def user_login(request):
    if request.method == "GET":
        login_form = LoginForm()
        context = {"login_form": login_form}
        return render(request, "userprofile/login.html", context)
    else:
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                # return redirect("article:article-list")
                # return redirect("index") 
                # return render(request, 'SmartCenter/trend.html', context)
                # return render(request, 'SmartCenter/your_template.html', {'context_data': data})
                # 数据查询，根据用户名查询出用户的权限
                authority = User.objects.get(username=data['username']).is_superuser & User.objects.get(username=data['username']).is_staff
                if authority:
                    # return redirect("BackManage") 
                    return redirect("MainInformation") 
                    
                else:
                    # return redirect("MainInformation")
                    return redirect("MainInformation_user") 

            else:
                context = {'obj': login_form, 'error': '账号或密码错误，请重新输入！'}
                return render(request, 'userprofile/login.html', context)
        else:
            context = {'obj': login_form, 'error': login_form.errors}
            return render(request, 'userprofile/login.html', context)


def user_logout(request):
    logout(request)
    return redirect("article:article-list")


def user_register(request):
    if request.method == 'GET':
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request, 'userprofile/register.html', context)
    else:
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()
            return redirect("userprofile:login")
        else:
            context = {'obj': register_form, 'error': register_form.errors}
            return render(request, 'userprofile/register.html', context)


def user_profile(request):
    if request.method == "GET":
        articles = ArticlePost.objects.filter(author_id=request.user.id)
        context = {'articles': articles}
        return render(request, 'userprofile/profile.html', context)
    else:
        profile = UserProfile.objects.get(id=request.user.id)
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form_data = profile_form.cleaned_data
            if 'avatar' in request.FILES:
                profile.avatar = profile_form_data['avatar']
            profile.save()
            return redirect('userprofile:profile')
        else:
            return HttpResponse('表单有误，请重新填写！')
