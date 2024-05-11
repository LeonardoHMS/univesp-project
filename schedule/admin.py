from django.contrib import admin

from .models import Schedule, TypeOfCut


class TypeOfCutAdmin(admin.ModelAdmin):
    list_display = ("type_cut", "value")
    search_fields = ("type_cut",)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "date_hour",
        "type_of_cut",
        "user",
        "conclude",
    )
    search_fields = ("type_of_cut",)


admin.site.register(TypeOfCut, TypeOfCutAdmin)
admin.site.register(Schedule, ScheduleAdmin)
