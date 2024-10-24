from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(label="",max_length=256)