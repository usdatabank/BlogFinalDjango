from django.contrib import admin
from .models import Post_Blog

# con esta linea luego de importar los modelos
# podremos usar el administrador de django para adminitrar nuestro blog
admin.site.register(Post_Blog)