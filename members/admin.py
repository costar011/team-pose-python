from django.contrib import admin
from . import models


@admin.register(models.MemberModel)
class MemberAdmin(admin.ModelAdmin):
    """ Member Admin Definition """

    list_display = (
        "name",
        "gender",
        "mobile",
        "email",
    )

    list_filter = ("gender",)
