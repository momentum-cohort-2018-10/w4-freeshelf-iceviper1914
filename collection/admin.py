from django.contrib import admin
from collection.models import Book
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title','author', 'description', 'brand',)
    # prepopulated_fields = {'slug': ('title',)}
admin.site.register(Book, BookAdmin)