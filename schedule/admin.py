from django.contrib import admin

from .models import Schedule, TypeOfCut


class TypeOfCutAdmin(admin.ModelAdmin):
    list_display = ("type", "value")
    search_fields = ("type",)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("day", "hour", "type_of_cut", "user")
    search_fields = ("day", "type_of_cut")


admin.site.register(TypeOfCut, TypeOfCutAdmin)
admin.site.register(Schedule, ScheduleAdmin)
