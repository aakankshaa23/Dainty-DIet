from .views import ProfileItemView,ShowView
from django.conf.urls import url

urlpatterns=[

url(r'^users/$',ShowView.as_view(),name='users'),
url(r'^(?P<username>[\w-]+)/$', ProfileItemView.as_view(),name='detail'),


]