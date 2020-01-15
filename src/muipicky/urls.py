"""muipicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from profiles.views import ProfileToggle,RegisterView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views
from menus.views import HomeView
from django.contrib import admin
from restaurants.views import RestaurantList,RestaurantCreateView,RestaurantUpdateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(),name='home'),
    url(r'^About/$', TemplateView.as_view(template_name='About.html'),name='about'),
    url(r'^restaurants/$',RestaurantList.as_view(),name='restaurants'),
    url(r'^items/',include('menus.urls',namespace='menus')),
    url(r'^u/',include('profiles.urls',namespace='profiles')),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^profile-follow/$',ProfileToggle.as_view(),name='follow'),
    url(r'^password-reset/$', auth_views.password_reset,name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done,name='password_reset_done'),
    url(r'^password-reset/complete/$',auth_views.password_reset_complete,name='password_reset_complete'),
    url(r'^password-reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/$',auth_views.password_reset_confirm,name='password_reset_confirm'),
    url(r'^restaurants/create/$', RestaurantCreateView.as_view(),name='restaurants-create'),
    url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantUpdateView.as_view(),name='detail'),
    #url(r'^restaurants/(?P<slug>[\w-]+)/edit/$',RestaurantUpdateView.as_view(),name='edit'),
  #  url(r'^restaurants/moga/$',MogaRestaurants.as_view()),
    url(r'^Contact/$', TemplateView.as_view(template_name='Contact.html'),name='contact'),
]
