from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Comment
from .forms import CommentForm
from blog.models import Post
from django.views import View
from django.shortcuts import render,reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

# commentaire
class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = self.request.user
            comment.save()
            messages.success(request, 'Votre commentaire a été ajouté avec succès.')
        else:
            messages.error(request, 'Une erreur est survenue. Veuillez vérifier le formulaire.')
        return redirect('blog:post_detail', pk=post.pk)
    

class CommentUpdateView(LoginRequiredMixin,UpdateView):
    model = Comment
    fields = ['text']
    template_name = 'comment/comment_form.html'

    def get_success_url(self):
        post_id = self.object.post.id
        return reverse('blog:post_detail', kwargs={'pk': post_id})
    
class CommentDeleteView(LoginRequiredMixin,DeleteView):
    model = Comment
    template_name = 'comment/comment_confirm_delete.html'

    def get_success_url(self):
        post_id = self.object.post.id
        return reverse('blog:post_detail', kwargs={'pk': post_id})
