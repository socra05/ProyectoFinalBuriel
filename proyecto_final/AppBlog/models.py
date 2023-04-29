from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    genero = models.CharField('Genero', max_length=90, blank=False, null=False)
    descripcion = models.CharField(
        'Descripcion', max_length=100, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.ImageField(
        null=True, blank=True, upload_to="imagen_genero")
    fecha = models.DateField(
        'Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['autor', '-fecha']

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f" {self.genero}, {self.imagen}"
