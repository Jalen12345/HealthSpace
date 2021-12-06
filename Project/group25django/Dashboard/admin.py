from django.contrib import admin
from . import models
from .models import index
# Register your models here.
admin.site.register(models.Sleep)
admin.site.register(models.Macro)
admin.site.register(models.index)
admin.site.register(models.Exercise)
