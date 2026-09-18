from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:id>/', views.post, name='post'),
    path('firstpage/', views.firstpage, name='firstpage'),
    path('secondpage/', views.secondpage, name='secondpage'),
    path('old_monk/', views.new_sample_page, name='old_monk'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('forgotpassword/', views.forgot_password, name='forgot_password'),
    path("reset_password/<uidb64>/<token>", views.reset_password, name="reset_password"),
    path("new_post/", views.new_post, name="new_post"),
    path("edit_post/<int:id>/", views.edit_post, name="edit_post"),
]
