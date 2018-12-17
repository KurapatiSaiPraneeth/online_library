from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth',)
    fields = ['first_name', 'last_name', ('date_of_birth')]



class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','summary','list_genre')
    inlines = [BooksInstanceInline]



@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_display = ('book','status','due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


# admin.site.register(Book)
# admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)