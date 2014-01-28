from django.contrib import admin
from django_bro_tables.models import (
    Regex, RegexEntry,
    Table, TableEntry,
)

class RegexEntryInline(admin.TabularInline):
    model = RegexEntry
    extra = 3

class RegexAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'disabled']
    inlines = [RegexEntryInline]

class RegexEntryAdmin(admin.ModelAdmin):
    search_fields = ['pattern', 'comment']
    list_display = ['regex', 'pattern', 'flags', 'comment', 'disabled']
    list_editable = ['pattern', 'flags', 'comment', 'disabled']
    list_filter = ['regex', 'disabled']
    date_hierarchy = 'date_added'


class TableEntryInline(admin.TabularInline):
    model = TableEntry
    extra = 3

class TableAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'num_fields']
    inlines = [TableEntryInline]

COLS = 'c0 c1 c2 c3 c4 c5'.split()

class TableEntryAdmin(admin.ModelAdmin):
    search_fields = COLS
    list_display = ['table'] + COLS
    list_editable = COLS

    date_hierarchy = 'timestamp'
    list_filter = ['table']
    

admin.site.register(Regex, RegexAdmin)
admin.site.register(RegexEntry, RegexEntryAdmin)

admin.site.register(Table, TableAdmin)
admin.site.register(TableEntry, TableEntryAdmin)
