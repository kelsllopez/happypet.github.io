from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "categoria","stock"]
    list_editable = ["precio"]
    search_fields = ["nombre","stock"]
    list_filter = ["categoria"]
    list_per_page = 10

admin.site.register(Categorias)
admin.site.register(Productos, ProductoAdmin)
admin.site.register(Contacto)
admin.site.register(Carro)
admin.site.register(Favorito)
admin.site.register(Mascota)
admin.site.register(Agengar_horas_disponibles)
admin.site.register(Comentario)
admin.site.register(Carrucel)
admin.site.register(PedirHora)
admin.site.register(Nosotros)

