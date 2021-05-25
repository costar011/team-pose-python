from django.contrib import admin
from . import models


class ContactFileInline(admin.TabularInline):
    model = models.ContactFileModel


@admin.register(models.ContactsModel)
class ContactsModelAdmin(admin.ModelAdmin):
    inlines = (ContactFileInline,)