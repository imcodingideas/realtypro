from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<int:user_id>/', views.view_profile, name='view_profile'),
    path('profile/<int:user_id>/edit', views.edit_profile, name='edit_profile'),
]
