from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.


def inicio(request):
    return render(request, 'AppBlog/inicio.html', {"post": obtener_post(request)})


@ login_required
def sobre_mi(request):
    return render(request, "AppBlog/sobre_mi.html")


# USUARIO

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "AppBlog/inicio.html", {"mensaje": "Cuenta creada correctamente", "post": obtener_post(request)})
        else:
            return render(request, "AppBlog/registro.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
    else:
        form = RegistroUsuarioForm()
        return render(request, "AppBlog/registro.html", {"form": form})


def login_usuarios(request):
    if request.method == "POST":
        form = LogUsuarioForm(request, data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario = info['username']
            contraseña = info['password']
            usuario = authenticate(username=usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppBlog/inicio.html", {"post": obtener_post(request)})
            else:
                return render(request, "AppBlog/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppBlog/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
    else:
        form = LogUsuarioForm()
        return render(request, "AppBlog/login.html", {"form": form})


@ login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.username = info['username']
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.save()
            return render(request, "AppBlog/inicio.html", {"post": obtener_post(request)})
        else:
            return render(request, "AppBlog/editar_perfil.html", {"form": form, "nombreusuario": usuario.username})
    else:
        form = UserEditForm()
        return render(request, "AppBlog/editar_perfil.html", {"form": form, "nombreusuario": usuario.username})


# PUBLICACIONES

@ login_required
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, "AppBlog/creacion_genero.html", {"form": form})


class detalle_genero(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'AppBlog/detalle_genero.html'


@ login_required
def eliminar_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return redirect("inicio")
    return render(request, "AppBlog/eliminar_post.html", {"post": post})


class EditarPost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditarPostForm
    success_url = reverse_lazy('inicio')
    context_object_name = 'post'
    template_name = 'AppBlog/editar_post.html'


def obtener_post(request):
    post = Post.objects.all()
    return post
