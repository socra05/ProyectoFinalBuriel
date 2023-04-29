from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('sobre_mi/', sobre_mi, name="sobre_mi"),
    # USUARIO
    path('login/', login_usuarios, name="login"),
    path('registro/', registro, name="registro"),
    path('logout/', LogoutView.as_view(template_name="AppBlog/logout.html"), name="logout"),
    path('editar_perfil/', editar_perfil, name="editar_perfil"),

    # PUBLICACIONES
    path('detalle_post/<int:pk>/', detalle_genero.as_view(), name='detalle_genero'),
    path('creacion_genero/', crear_post, name="crear_post"),
    path('eliminar_post/<int:id>/', eliminar_post, name="eliminar_post"),
    path('editar_post/<int:pk>/',
         EditarPost.as_view(), name='editar_post'),

]
