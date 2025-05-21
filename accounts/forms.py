from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate


class CustomerSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number']

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if CustomUser.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError("This mobile number is already registered.")
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'customer'
        user.set_password(user.phone_number)  # set phone number as password
        if commit:
            user.save()
        return user


class CustomerLoginForm(forms.Form):
    username = forms.CharField()
    phone_number = forms.CharField(label='phone number')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        phone_number = cleaned_data.get('phone_number')

        if username and phone_number:
            try:
                user = CustomUser.objects.get(username=username, phone_number=phone_number)
            except CustomUser.DoesNotExist:
                raise forms.ValidationError("No user with these specifications was found.")

            if not user.check_password(phone_number):
                raise forms.ValidationError("password is not correct.")

            cleaned_data['user'] = user

        return cleaned_data
