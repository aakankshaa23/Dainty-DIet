from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect

import random
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from .models import RestaurantLocation
from .forms import RestaurantForm,ModelCreateForm

class RestaurantList(LoginRequiredMixin, ListView):
	template_name='restaurants/restaurant_list.html'
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)





class RestaurantCreateView(LoginRequiredMixin,CreateView):
	form_class=ModelCreateForm
	template_name='form.html'
	login_url='/login/'
	success_url='/restaurants/'

	def form_valid(self,form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		return super(RestaurantCreateView,self).form_valid(form)
	def get_context_data(self,*args,**kwargs):
		return super(RestaurantCreateView,self).get_context_data(*args,**kwargs)
		context['title']='Add Restaurants'
		return context


class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
	form_class=ModelCreateForm
	template_name='restaurants/detail-update.html'
	login_url='/login/'
	#success_url='/restaurants/'

	def get_context_data(self,*args,**kwargs):
		return super(RestaurantUpdateView,self).get_context_data(*args,**kwargs)
		context['title']='Update '
		return context
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

