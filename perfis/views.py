from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
	perfis = Perfil.objects.all()
	user = get_user_logado(request)
	contatos_user = get_contatos_user(request)
	val = {'perfis':perfis,'perfil_logado':user,'contatos':contatos_user}
	return render(request, 'index.html', val)
	

@login_required
def exibir(request, perfil_id):	
	perfil = Perfil.objects.get(id=perfil_id)
	isContato = is_contato(request, perfil)
	val = {'perfil' : perfil, 'is_contato' : isContato}
	return render(request, 'perfil.html', val)


@login_required
def convidar(request, perfil_id):
	perfil_logado = get_user_logado(request)
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')

@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')


@login_required
def regeitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.recusar()
	return redirect('index')


@login_required
def remover_contato(request, contato_id):
	contato = Perfil.objects.get(id=contato_id)
	get_user_logado(request).contatos.remove(contato)
	return redirect('index')


@login_required
def get_contatos_user(request):
	return get_user_logado(request).contatos.all()


def is_contato(request, perfil):
	perfil_logado = get_user_logado(request)
	return perfil in perfil_logado.contatos.all()


def get_user_logado(request):
	return Perfil.objects.get(id=1)