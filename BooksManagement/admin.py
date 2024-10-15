from django.contrib import admin, messages
from . import models


class BookInline(admin.StackedInline):
    model = models.Book
    extra = 0

class BorrowedBookInline(admin.StackedInline):
    model = models.BorrowedBook
    extra = 1

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['id', 'name', 'family']
    search_fields = ['name', 'family']
    sortable_by = ['id']
    list_editable = ['name', 'family']
    search_fields = ['name', 'family']
    inlines = [BookInline]
    
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['id', 'name']


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Info', {'fields': ('title', 'author')}),
        ('Details', {'fields': ('isbn', 'summary', 'category', 'is_available', 'id')}),
    )
    readonly_fields = ['id']
    list_display = ['id', 'title', 'isbn', 'is_available', 'author']
    list_editable = ['is_available']
    inlines = [BorrowedBookInline]
    actions = ['no_available', 'available']
    
    def no_available(self, request, queryset):
        queryset.update(is_available=False)
        self.message_user(request, f"{queryset.count()} books have been marked as unavailable.", messages.SUCCESS)
    no_available.short_description = "Mark selected books as unavailable"

    def available(self, request, queryset):
        queryset.update(is_available=True)
        self.message_user(request, f"{queryset.count()} books have been marked as available.", messages.SUCCESS)
    available.short_description = "Mark selected books as available"
    
    

@admin.register(models.BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'borrowed_book', 'return_date']
