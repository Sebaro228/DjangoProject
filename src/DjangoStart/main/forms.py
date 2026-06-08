from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Ваше ім'я",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': "Введіть ваше ім'я"
        })
    )
    email = forms.EmailField(
        label="Ваш Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': "name@example.com"
        })
    )
    subject = forms.CharField(
        max_length=200,
        label="Тема повідомлення",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': "Тема звернення"
        })
    )
    message = forms.CharField(
        label="Текст повідомлення",
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'rows': 6,
            'placeholder': "Напишіть ваше повідомлення тут..."
        })
    )