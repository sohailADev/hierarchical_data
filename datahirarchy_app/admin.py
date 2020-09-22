from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
from . import models
# Register your models here.
admin.site.register(models.Folder,DraggableMPTTAdmin)
admin.site.register(models.Author)