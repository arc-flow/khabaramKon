from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'مشخصات ماشینی که میخوای رو بنویس', 'class':'form-control','style':'line-height: 2.5'}), label="",max_length=256)