from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

# ✅ نموذج تسجيل الدخول بالبريد الإلكتروني
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='البريد الإلكتروني')

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("البريد الإلكتروني أو كلمة المرور غير صحيحة.")
        return self.cleaned_data


# ✅ نموذج إنشاء حساب مخصص يحتوي على الحقول الإضافية
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='البريد الإلكتروني',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'example@email.com'})
    )
    country_code = forms.CharField(
        label='مفتاح الدولة',
        required=True,
        initial='+966',
        widget=forms.TextInput(attrs={'placeholder': '+966'})
    )
    phone_number = forms.CharField(
        label='رقم الجوال',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '5xxxxxxxx'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'country_code', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.country_code = self.cleaned_data['country_code']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user
