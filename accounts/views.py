from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        # 사용자 회원가입 로직
        pass
    else:
        return render(request, 'accounts/signup.html')
