from django.urls import path
from .views import Comentarios

urlpatterns = [
    path('inicio/<int:pk>/comentario/',
         Comentarios.as_view(), name='comentario'),

]
