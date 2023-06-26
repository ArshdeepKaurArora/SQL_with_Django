from django.contrib import admin

from .models import Book, Author, Address, Country

class BookAdmin(admin.ModelAdmin):
    """Key features for data shown on adming webpage."""
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("ranking",)
    list_display = ("title", "author",)
    # readonly_fields = ("slug",)


# Register your models here.

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
