from django.contrib import admin
from .models import Table1, Table2
# Register your models here.
class Table2Inline(admin.TabularInline):
    model = Table2
    extra = 1

@admin.register(Table1)
class Table1Admin(admin.ModelAdmin):
    inlines = [Table2Inline]

@admin.register(Table2)
class Table2Admin(admin.ModelAdmin):
    list_display = ('desc','images','table1_name')
    

    def table1_name(self, obj):
        return obj.table1.name

    table1_name.short_description = 'Table1 Name'
