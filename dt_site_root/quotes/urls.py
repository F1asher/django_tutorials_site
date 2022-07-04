from . import views
from .views import QuoteList, QuoteView

from django.urls import path


urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('show/<int:pk>', QuoteView.as_view(), name='quote-detail'),
    path('show', QuoteList.as_view(), name='showquotes'),
]
