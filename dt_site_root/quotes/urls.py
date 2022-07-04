from . import views

from django.urls import path


urlpatterns = [
    path('', views.quote_req, name='quote-request'),
]
