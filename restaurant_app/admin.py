from django.contrib import admin
from .models import Item

# inherits from admin as interface
# this is build admin module that allow uer login
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status')
    list_filter=('status',)
    search_fields = ('meal','description')
    
admin.site.register(Item, MenuItemAdmin)