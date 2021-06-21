from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioPersCreationForm, UsuarioPersChangeForm
from .models import UsuarioPers,Viaje,Hospedaje,Ciudad,Vuelo,ComentarioVuelo,ComentarioHosp,ComentarioViaje


#creacion y visualizacion de los comentarios
class ComentarioInLine(admin.TabularInline):
    model = ComentarioVuelo

#creacion y visualizacion del usuario personalizado
class UsuarioPersAdmin(UserAdmin):
    add_form = UsuarioPersCreationForm
    form = UsuarioPersChangeForm
    model = UsuarioPers
    list_display = ['email', 'username', 'edad' , 'telefono','genero', 'is_staff',]

# Register your models here.
#registro de los modelos para poder visualizarlos el admin
admin.site.register(UsuarioPers,UsuarioPersAdmin)
admin.site.register(Viaje)
admin.site.register(Hospedaje)
admin.site.register(Ciudad)
admin.site.register(Vuelo)
admin.site.register(ComentarioVuelo)
admin.site.register(ComentarioHosp)
admin.site.register(ComentarioViaje)

