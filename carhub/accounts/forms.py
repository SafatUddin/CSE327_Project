from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPES, widget=forms.RadioSelect, label="I am a")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_type_choice = self.cleaned_data.get('user_type')
            UserProfile.objects.create(user=user, user_type=user_type_choice)
        return user