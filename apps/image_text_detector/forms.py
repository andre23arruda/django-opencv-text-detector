from django import forms


class ImageInputForms(forms.Form):
    image = forms.FileField(
        label='Selecione uma imagem para localizar texto',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
        })
    )