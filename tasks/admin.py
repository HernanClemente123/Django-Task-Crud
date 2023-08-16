from django.contrib import admin
from .models import Task

#creamos una clase que no permitira ver el campo 'created' (solo lectura)
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

# Register your models here.
admin.site.register(Task, TaskAdmin)