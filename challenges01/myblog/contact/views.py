from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.mail import send_mail
from django.conf import settings

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('contact:success_page')

    def form_valid(self, form):
        # Associer l'utilisateur connecté
        form.instance.user = self.request.user
        response = super().form_valid(form)

        # Envoyer un email à l'utilisateur
        subject = f"Confirmation de votre message : {form.instance.subject}"
        message = f"Bonjour {self.request.user.username},\n\n" \
                f"Merci de nous avoir contacté. Nous avons bien reçu votre message :\n\n" \
                f"{form.instance.message}\n\n" \
                f"Nous reviendrons vers vous dans les plus brefs délais.\n\n" \
                f"Cordialement,\nL'équipe de support."

        # Envoyer l'email à l'utilisateur connecté
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [self.request.user.email],  # Envoyer l'email à l'utilisateur
            fail_silently=False,
        )

        return response

def success_page(request):
    return render(request, 'contact/success.html')
