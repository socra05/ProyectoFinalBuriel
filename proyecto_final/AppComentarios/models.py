from django.db import models
from AppBlog.models import Post


# Create your models here.


class Comentario(models.Model):
    nombre = models.CharField(max_length=40)
    comentario = models.ForeignKey(
        Post, related_name='comentarios', on_delete=models.CASCADE, null=True)
    mensaje = models.TextField(null=True, blank=True)
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_comentario']

    def __str__(self):
        return f"{self.nombre} {self.comentario}"
