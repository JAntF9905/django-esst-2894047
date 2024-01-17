from django.contrib import admin

from . import models


# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')
    list_display=('title',)

admin.site.register(models.Note, NotesAdmin)