from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # settings.AUTH_USER_MODEL 에 등록한 정보 반환해주는 모델 => boards.User 에서 불러오겠당
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    # 모델에 대한 정보가 담기는 곳
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
