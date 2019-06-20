from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
# 밑에 내가 만든 login 함수와 이름이 겹쳐서 이름을 지정해주기
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .forms import CustomUserChangeForm, CustomUserCreationForm


@require_GET
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method == 'POST':
        # 사용자 회원가입 로직
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():   # form 이 유효하다면 저장
            user = form.save()
            return redirect('boards:index', user)
    else:  # GET accounts/signup/
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)  # 회원가입이 안 되었을 때 다시 로그인 페이지 보여주기


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:  # 이미 login 되어있다면 다시 login page 뜨지 않고 index page 로 가도록 설정
        return redirect('boards:index')

    if request.method == "POST":
        # 로그인 로직 실행
        form = AuthenticationForm(request, request.POST)

        # 사용자 입력 유효성 검사
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'boards:index')
    else:  # GET /accounts/login/ => html 페이지만 렌더링

        form = AuthenticationForm
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


@require_GET
def logout(request):
    # 로그아웃 로직
    auth_logout(request)
    return redirect('boards:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if not request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == "POST":
        # 업데이트 로직 수행
        form = CustomUserChangeForm(request.POST, instance=request.user)  # 사용자가 입력한 상태로 새로운 form 생성
        if form.is_valid():
            form.save()
            return redirect('boards:index')

    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        # 비밀번호 변경 로직
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 세션의 정보와 회원의 정보가 달라져서 세션을 유지한 상태로 새롭게 업데이트
            update_session_auth_hash(request, request.user)
            return redirect('boards:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)


@require_POST
def delete(request):
    # 유저 삭제 로직
    request.user.delete()
    return redirect('boards:index')





