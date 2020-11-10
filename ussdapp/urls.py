from django.conf.urls import url
from django.urls import path
from . import views
from ussdapp.views import UssdList

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^ussd',views.ussd,name = 'ussd'),
    url(r'^api/ussd/$', views.UssdList.as_view())
    # path('ussd/', UssdList.as_view(),  name='ussd'),
]