from .models import *
from django import forms



class CipherForm(forms.ModelForm):
    class Meta:
        model = Cipher
        fields = '__all__'


class DecryptCipherForm(forms.ModelForm):
    class Meta:
        model = Cipher
        fields = '__all__'
