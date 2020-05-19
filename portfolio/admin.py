from django.contrib import admin
from .models import Portfolio, Technology


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'percent', 'rank', 'show')


admin.site.register(Portfolio)
admin.site.register(Technology, TechnologyAdmin)
