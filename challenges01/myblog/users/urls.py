from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, ProfileUpdateView,UserLoginView,ProfileDetailView,UserLogoutView

app_name= 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('profile/', ProfileUpdateView.as_view(), name='profile'),
]

