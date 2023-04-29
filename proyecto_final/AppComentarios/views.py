from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comentario
from .forms import ComentarioForm
from django.urls import reverse_lazy

# Create your views here.


class Comentarios(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'AppBlog/comentarios.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(Comentarios, self).form_valid(form)
