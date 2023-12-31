from django.contrib import admin

from library.models import Book, Collection, Links, CharacterStorie
from library.models import Text, History, Quotes, Character

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('text',)
    
    def display_quotes(self, obj):
        return ', '.join([link.quote for link in self.quotes.all()[:10]])


class BookAdmin(admin.ModelAdmin):
    list_display = ('name','chapters','collection','testament')
    
    search_fields = ('name', 'collection')
    
    ordering = ('collection',)
    
    def testament(self, obj):
        testament = Collection.objects.get(id=obj.collection_id)
        return "Antiguo Testamento" if testament.section == 'AT' else "Nuevo Testamento"
    
    
class TextAdmin(admin.ModelAdmin):
    list_display = ('book','history','chapter','verse','description')
    
    ordering = ('history','chapter','verse',)
    
    search_fields = ('history',)

@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('name','text',)
    
    search_fields = ('name',)
    
    ordering = ('-id',)
    
    admin.site.site_title = 'citas'
    
@admin.register(CharacterStorie)
class CharacterStorieAdmin(admin.ModelAdmin):
    list_display = ('character', 'display_stories',)
    
    search_fields = ('character',)
    
    ordering = ('character',)
    
    def display_stories(self, obj):
        return ', '.join([story.title for story in obj.stories.all()[:5]])
    
    display_stories.short_description = 'History'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name','number_books',)

    def number_books(self, obj):
        return Book.objects.filter(collection=obj).count()

admin.site.site_header = 'Bible Graph'
admin.site.index_title = 'Panel de control de mi sitio'



admin.site.register(Book, BookAdmin)

admin.site.register(Text, TextAdmin)
admin.site.register(History)
admin.site.register(Character)
