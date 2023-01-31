from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Producto, Account

class ProductoForm(forms.ModelForm):
    class Meta:
        model= Producto
        exclude =  exclude = ['idProducto']


class RegistrationForm(UserCreationForm, forms.ModelForm):
	class Meta:
		model =Account
		fields = ('firstname','lastname','email', 'username', 'password1', 'password2',)
	
	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)
	# class Meta:
        
	# 	model = Account
    #     address1= AddressField()
	# 	fields = ('email', 'username', 'password1', 'password2', )

	# def clean_email(self):
	# 	email = self.cleaned_data['email'].lower()
	# 	try:
	# 		account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
	# 	except Account.DoesNotExist:
	# 		return email
	# 	raise forms.ValidationError('Email "%s" is already in use.' % account)

	# def clean_username(self):
	# 	username = self.cleaned_data['username']
	# 	try:
	# 		account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
	# 	except Account.DoesNotExist:
	# 		return username
	# 	raise forms.ValidationError('Username "%s" is already in use.' % username)