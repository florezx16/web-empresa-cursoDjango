from django import forms

class contactForm(forms.Form):
    name = forms.CharField(max_length=100,label='Name',widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu nombre'}
    ))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Escribe tu correo'}
        ))
    content = forms.CharField(max_length=100,label='Content',widget=forms.Textarea(
        attrs={'class':'form-control','rows':3,'placeholder':'Escribe tu mensaje'}
    ))