from django.contrib import admin
from .models import Profile  # Assurez-vous d'importer votre modèle Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'birth_date')  # Champs à afficher dans la liste
    search_fields = ('user__username', 'location')  # Champs recherchables
    list_filter = ('location',)  # Filtres pour affiner la recherche
    ordering = ('user',)  # Tri par utilisateur

    fieldsets = (
        (None, {
            'fields': ('user', 'bio', 'location', 'birth_date', 'avatar')
        }),
    )
