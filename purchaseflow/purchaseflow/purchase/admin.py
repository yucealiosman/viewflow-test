from django.contrib import admin

# Register your models here.

from . import models


admin.site.register(models.Leave)
admin.site.register(models.Developer)
admin.site.register(models.Manager)
