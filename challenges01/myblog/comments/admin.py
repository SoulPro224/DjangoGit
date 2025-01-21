from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')  # Retiré 'is_approved'
    search_fields = ('author__username', 'text')
    list_filter = ('created_at',)  # Retiré 'is_approved'
    ordering = ('-created_at',)

# admin.site.register(Comment, CommentAdmin)