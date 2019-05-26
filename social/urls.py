from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', auth_views.LoginView.as_view(template_name= 'social/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page= 'homepage'), name='logout'),
    path('wall/<int:id_profil>', views.wall, name='wall'),
    path('getcomment/<int:id_profil>/<int:id_post>', views.wall, name='getcomment'),
    
]