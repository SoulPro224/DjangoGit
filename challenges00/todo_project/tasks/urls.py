from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.task_list, name='task_list'),
    path('ajout/', views.task_create, name='task_create'),
    path('edit/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]

# from django.urls import path,include
# from .views import task_list, task_create, task_update, task_delete,signup
# from . import views

# app_name = 'tasks'
# urlpatterns = [
#     path('', task_list, name='task_list'),
#     path('new/', task_create, name='task_create'),
#     path('edit/<int:pk>/', task_update, name='task_update'),
#     path('delete/<int:pk>/', task_delete, name='task_delete'),
#     # Auth URLs
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('accounts/signup/', views.signup, name='signup'),
# ]
