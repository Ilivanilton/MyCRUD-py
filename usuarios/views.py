from django.shortcuts import render, redirect
from django.views.generic.base import View
from forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from perfis.models import Perfil


class RegistrarUsuarioView(View):

    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
    	form = RegistrarUsuarioForm(request.POST)

    	if form.is_valid():
    		d = form.data
    		user = User.objects.create_user(d['nome'],d['email'],d['senha'])
    		perfil = Perfil(nome=d['nome'], email=d['email'], usuario=user)
    		perfil.save()
    		return redirect('index')

        return render(request, self.template_name , {'form' : form})