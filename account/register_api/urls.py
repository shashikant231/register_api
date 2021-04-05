from django.urls import path
from django.urls.resolvers import URLPattern
from  account.register_api.views import registration_view


app_name  = 'account'
urlpatterns = [
    path('',registration_view,name="register"),
    ]
