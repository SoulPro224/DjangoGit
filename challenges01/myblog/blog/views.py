from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from .models import Post,Category,Tag
from .forms import PostForm
from comments.forms import CommentForm
from comments.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

# Liste des articles (affichage ordonné par date de publication)
# class PostListView(LoginRequiredMixin, ListView):
#     model = Post
#     template_name = 'blog/home.html'
#     context_object_name = 'posts'
#     queryset = Post.objects.select_related('author').order_by('-published_at')
#     paginate_by = 10  # Nombre d'articles par page

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         category = self.request.GET.get('category')
#         if category:
#             queryset = queryset.filter(category__name__iexact=category)
#         return queryset
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # paginate_by = 6  # Pagination si besoin

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtrage par catégorie et tag
        category = self.request.GET.get('category', None)
        tag = self.request.GET.get('tag', None)

        if category:
            queryset = queryset.filter(category__name=category)
        if tag:
            queryset = queryset.filter(tags__name=tag)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['selected_category'] = self.request.GET.get('category', None)
        context['selected_tag'] = self.request.GET.get('tag', None)
        return context

# Détail d'un article
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupérer les commentaires associés à ce post
        comments = Comment.objects.filter(post=self.object).order_by('-created_at')
        context['comments'] = comments  # Ajouter les commentaires au contexte
        context['form'] = CommentForm()  # Ajouter le formulaire de commentaire au contexte
        return context

# Création d'un article (seuls ceux qui ont la permission de publier peuvent créer)
class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:home')
    permission_required = 'blog.can_publish_post'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm(self.permission_required):
            raise PermissionDenied("Vous n'avez pas la permission de publier un article.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'L\'article a été créé avec succès !')
        return super().form_valid(form)

# Mise à jour d'un article (seuls les auteurs ou ceux avec la permission peuvent éditer)
class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:home')
    permission_required = 'blog.can_edit_post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user and not self.request.user.has_perm(self.permission_required):
            raise PermissionDenied("Vous n'avez pas la permission de modifier cet article.")
        return obj

    def form_valid(self, form):
        messages.success(self.request, 'L\'article a été mis à jour avec succès !')
        return super().form_valid(form)

# Suppression d'un article (seuls ceux qui ont la permission peuvent supprimer)
class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:home')
    permission_required = 'blog.can_delete_post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user and not self.request.user.has_perm(self.permission_required):
            raise PermissionDenied("Vous n'avez pas la permission de supprimer cet article.")
        return obj

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'L\'article a été supprimé avec succès.')
        return super().delete(request, *args, **kwargs)

class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category_post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        # Récupérer la catégorie, sinon renvoyer une 404
        category = get_object_or_404(Category, name=category_name)
        # Retourner les articles triés par date de publication
        return Post.objects.filter(category=category).order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajouter la catégorie au contexte pour l'utiliser dans le template
        context['category'] = get_object_or_404(Category, name=self.kwargs['category_name'])
        return context

class TagPostListView(ListView):
    model = Post
    template_name = 'blog/tag_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.kwargs['tag_name'])
        # Retourner les articles liés au tag
        return Post.objects.filter(tags=tag).order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajouter le tag au contexte pour l'utiliser dans le template
        context['tag'] = get_object_or_404(Tag, name=self.kwargs['tag_name'])
        return context

