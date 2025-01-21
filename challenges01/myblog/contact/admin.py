from django.contrib import admin
from .models import Contact

# Configuration de l'administration pour le modèle Contact
class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)
