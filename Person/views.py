from django.shortcuts import render, redirect
from Person.models import MyUser, User
from django.views.generic import TemplateView,View
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from . import models
# Create your views here.

class ListaFollow(TemplateView):
	template_name = 'lista_follow.html'

	def get_context_data(self,**kwargs):
		context = super(ListaFollow,self).get_context_data(**kwargs)
		context['all'] = MyUser.objects.all()
 		context['me'] = User.objects.get(username=self.request.user)
		context['notme'] = MyUser.objects.filter(follow__username=self.request.user)
		context['notfollow'] = MyUser.objects.filter(~Q(follow__username=self.request.user))
		return context

class AddFollow(View):
	def get(self,request, id):
		me = models.MyUser.objects.get(username=request.user) #soy yo
		followed = models.MyUser.objects.get(id=id) #el wey
		me.follow.add(followed)#relacion
		return redirect(reverse('lista_follow'))

class RemoveFollow(View):
	def get(self,request, id):
		me = models.MyUser.objects.get(username=request.user) #instancia del usuario con el id que quiero crear
		followed = models.MyUser.objects.get(id=id)
		me.follow.remove(followed) #creo el usuario con mi nombre y la relacion
		return redirect(reverse('lista_follow'))