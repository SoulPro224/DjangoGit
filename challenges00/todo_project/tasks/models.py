from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('1', 'Faible'),
        ('2', 'Moyenne'),
        ('3', 'Élevée'),
    ]

    CATEGORY_CHOICES = [
        ('personal', 'Personnel'),
        ('work', 'Travail'),
        ('other', 'Autre'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='1')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='personal')

    def __str__(self):
        return self.title

# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     due_date = models.DateTimeField(default=timezone.now)  # Date d'échéance
#     priority = models.PositiveIntegerField(default=1)  # Priorité (1 = Faible, 2 = Moyenne, 3 = Haute)
#     complete = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE,null=True, blank=True)

#     def __str__(self):
#         return self.title




