from .models import Author, Post
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

class SignUpForm(UserCreationForm):
    class Meta:
        model = Author
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar', 'birthdate', 'profession' ,'password1', 'password2')
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }

class PostForm(forms.ModelForm):
    bbcode_content = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    class Meta:
        model = Post
        fields = ['title', 'content', 'bbcode_content']
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }
