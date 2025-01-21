from django.db import models
from django.contrib.auth.models import User
from blog.models import Post  # Assurez-vous d'importer le modèle Post depuis l'application blog
from django.utils import timezone

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commentaire de {self.author} sur {self.post.title}'
