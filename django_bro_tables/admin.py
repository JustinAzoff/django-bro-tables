from django.contrib import admin
from django_bro_tables.models import Regex, RegexEntry

class RegexEntryInline(admin.TabularInline):
    model = RegexEntry
    extra = 3

class RegexAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'disabled']
    inlines = [ RegexEntryInline ] 

class RegexEntryAdmin(admin.ModelAdmin):
    search_fields = ['pattern', 'comment']
    list_display = ['regex', 'pattern', 'flags', 'comment', 'disabled']
    list_editable = ['pattern', 'flags', 'comment', 'disabled']
    list_filter = ['disabled']
    

admin.site.register(Regex, RegexAdmin)
admin.site.register(RegexEntry, RegexEntryAdmin)
