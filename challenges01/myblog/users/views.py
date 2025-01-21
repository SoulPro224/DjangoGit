from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from django.views import generic 
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, UserProfileForm
from .models import Profile
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)

        # Création automatique du profil
        Profile.objects.create(user=user)

        # Gestion d'erreur pour s'assurer que le groupe existe
        try:
            group = Group.objects.get(name='visiteur')
            user.groups.add(group)
        except Group.DoesNotExist:
            # Logger ou créer le groupe si non existant
            group = Group.objects.create(name='visiteur')
            user.groups.add(group)

        login(self.request, user)
        return response


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        # Retourne le profil de l'utilisateur connecté
        return self.request.user.profile


# class UserLoginView(LoginView):
#     template_name = 'users/login.html'  # Chemin vers le template de connexion
#     success_url = reverse_lazy('users:profile')   # Redirige après connexion réussie

class UserLoginView(LoginView):
    template_name = 'registration/login.html'  # Chemin vers le template de connexion
    success_url = reverse_lazy('blog:home')  # Redirection après connexion réussie

    def get_success_url(self):
        # Si l'utilisateur est redirigé depuis une autre page, le rediriger vers cette page
        return self.get_redirect_url() or self.success_url


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile
    

class UserLogoutView(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy('users:login')

