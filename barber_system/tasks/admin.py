from django.contrib import admin

from .models import Task, TipoCorte, Corte

# Register your models here.

admin.site.register(Task)
admin.site.register(TipoCorte)
admin.site.register(Corte)
