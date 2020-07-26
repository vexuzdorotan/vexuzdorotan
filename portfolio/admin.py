from django.contrib import admin
from .models import Portfolio, Technology, Application


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank', 'show')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank', 'show')


admin.site.register(Portfolio)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Application, ApplicationAdmin)
