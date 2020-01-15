
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404,redirect
from restaurants.models import RestaurantLocation
from django.db.models import Q
from django.views.generic import DetailView,View,CreateView
from menus.models import Item
from .models import Profile
from django.http import Http404
from .forms import RegisterForm
# Create your views here.
User=get_user_model()
class RegisterView(CreateView):
	form_class=RegisterForm
	template_name='registration/form-register.html'
	success_url='/'

class ShowView(LoginRequiredMixin ,View):
	def get(self,request,*args,**kwargs):
		data=User.objects.all();
		return render(request,'profiles/users.html',{"data":data})
	# def get_context_data(self,*args,**kwargs):
	# 	context=super(ShowView,self).get_context_data(*args,**kwargs)
	# 	data=User.objects.all()
	# 	context['data']=data
	# 	return context

class ProfileToggle(LoginRequiredMixin,View):
	def post(self,request,*args,**kwargs):
		user_to_toggle=request.POST.get("username").strip()
		profile_ =Profile.objects.get(user__username__iexact=user_to_toggle)
		user_login=request.user
		if user_login in profile_.followers.all():
			profile_.followers.remove(user_login)
		else:
			profile_.followers.add(user_login)
		return redirect(f"/u/{user_to_toggle}/")

class ProfileItemView(DetailView):
	template_name='profiles/user.html'
	def get_object(self):
		username=self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User,username__iexact=username,is_active=True)
	def get_context_data(self,*args,**kwargs):
		context=super(ProfileItemView,self).get_context_data(*args,**kwargs)
		user=context['user']
		is_following=False
		if user.profile in self.request.user.is_following.all():
			is_following=True
		context['is_following']=is_following
		qs=RestaurantLocation.objects.filter(owner=user)
		query=self.request.GET.get('q')
		print(query)
		if query:
			query=query.strip()
			qs=qs.filter(Q(name__icontains=query) | Q(location__icontains=query)|Q(category__icontains=query)|Q(item__contents__icontains=query)).distinct()
		items_exists=Item.objects.filter(user=user).exists()
		if qs.exists() and items_exists:
			context['locations']=qs
		return context



