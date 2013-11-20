from django.contrib import admin
from django_bro_tables.models import (
    Regex, RegexEntry,
    Table, TableEntry,
)

class RegexAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'disabled']

class RegexEntryAdmin(admin.ModelAdmin):
    search_fields = ['pattern', 'comment']
    list_display = ['regex', 'pattern', 'flags', 'comment', 'disabled']
    list_editable = ['pattern', 'flags', 'comment', 'disabled']
    list_filter = ['regex', 'disabled']
    date_hierarchy = 'date_added'

class TableAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'num_fields']

COLS = 'c0 c1 c2 c3 c4 c5'.split()

class TableEntryAdmin(admin.ModelAdmin):
    search_fields = ['pattern', 'comment']
    list_display = ['table'] + COLS
    list_editable = COLS
    

admin.site.register(Regex, RegexAdmin)
admin.site.register(RegexEntry, RegexEntryAdmin)

admin.site.register(Table, TableAdmin)
admin.site.register(TableEntry, TableEntryAdmin)
