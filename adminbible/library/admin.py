from django.contrib import admin

from library.models import Book, Collection, Links, CharacterStorie
from library.models import Text, History, Quotes, Character


class LinksAdmin(admin.ModelAdmin):
    list_display = ('text',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name','chapters','collection',)
    
# class HistoryAdmin(admin.ModelAdmin):
#     list_display = ('book','chapter','title',)
    
class TextAdmin(admin.ModelAdmin):
    list_display = ('book','history','chapter','verse','description')
    
    ordering = ('-history','chapter','verse',)
    
    search_fields = ('history',)


class QuotesAdmin(admin.ModelAdmin):
    list_display = ('name','text',)
    
    search_fields = ('name',)
    
    ordering = ('name',)
    
    admin.site.site_title = 'citas'
    
admin.site.site_header = 'Bible Graph'
admin.site.index_title = 'Panel de control de mi sitio'



admin.site.register(Book, BookAdmin)
admin.site.register(Collection)

admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(History)
admin.site.register(Links, LinksAdmin)
admin.site.register(Character)
admin.site.register(CharacterStorie)
