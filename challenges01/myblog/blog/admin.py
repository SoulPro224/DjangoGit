from django.contrib import admin
from .models import Post, Tag , Category # Remplacez par vos modèles

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'category')
    search_fields = ('title', 'content')
    list_filter = ('published_at', 'author', 'category')
    ordering = ('-published_at',)

# admin.site.register(Post, PostAdmin)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# admin.site.register(Tag, TagAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
# admin.site.register(Category, CategoryAdmin)