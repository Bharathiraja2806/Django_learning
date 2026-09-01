from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:id>/', views.post, name='post'),
    path('firstpage/', views.firstpage, name='firstpage'),
    path('secondpage/', views.secondpage, name='secondpage'),
    path('old_monk/', views.new_sample_page, name='old_monk'),
]

