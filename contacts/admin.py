from django.contrib import admin
from . import models


@admin.register(models.ContactsModel)
class ContactModelAdmin(admin.ModelAdmin):
    pass
