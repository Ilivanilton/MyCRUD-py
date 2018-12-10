from django import forms
from django.contrib.auth.models import User


class RegistrarUsuarioForm(forms.Form):

	nome = forms.CharField(required=True)
	email = forms.CharField(required=True)
	senha = forms.CharField(required=True)

	def is_valid(self):
		valid = True
		if not super(RegistrarUsuarioForm, self).is_valid():
			msg = 'Verifique os dados digitados'
			self.adiciona_erro(msg)
			valid = False	

		user_exists = User.objects.filter(username=self.data['nome']).exists()
		if user_exists:
			self.adiciona_erro('User ja existente')
			valid = False

		return valid

	def adiciona_erro(self, msg):
		erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		erros.append(msg)