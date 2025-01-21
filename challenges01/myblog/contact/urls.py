from django.urls import path
from .views import ContactCreateView
from . import views

app_name = 'contact'
urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('success/', views.success_page, name='success_page'),
]
