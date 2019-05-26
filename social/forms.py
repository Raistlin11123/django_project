from django import forms
from .models import Post, Profil, CommentPost

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={'class': ''}),
        }


