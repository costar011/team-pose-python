from django.contrib import admin
from . import models


@admin.register(models.MemberModel)
class MemberAdmin(admin.ModelAdmin):
    """ Member Admin Definition """

    pass
