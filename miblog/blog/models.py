from pyexpat import model
from django.db import models
from django.conf import settings
from django.utils import timezone

# creamos el modelo para los post
class Post_Blog(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto_contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    #creamos el metodo que publicara
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save

    def __str__(self):
        return self.titulo