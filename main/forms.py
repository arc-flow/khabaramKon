from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'مشخصات ماشینی که میخوای رو بنویس', 'class':'form-control','style':'line-height: 2.5'}), label="",max_length=256)

class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'شماره موبایل ت رو بنویس', 'class':'form-control'}), label="",max_length=11)

class VerifyOTPForm(forms.Form):
    otp = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'کد تایید پیامک شده رو بنویس', 'class':'form-control'}), label="",max_length=4)