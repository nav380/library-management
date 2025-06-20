from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, Issue

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'issue_date', 'due_date', 'return_date', 'returned')
    readonly_fields = ('issue_date', 'due_date', 'return_date')
    fieldsets = (
        (None, {'fields': ('book', 'user', 'issue_date', 'due_date', 'return_date', 'returned')}),
    )
    list_filter = ('issue_date', 'due_date', 'return_date')
    search_fields = ('book__title', 'user__username')
    ordering = ('issue_date',)
    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'isbn',
        'publication_date',
        'pages',
        'language',
        'publisher',
        'serial_number',
        'numberofcopies',
        'available_copies',
    )
    search_fields = ('title', 'author', 'isbn', 'serial_number')
    list_filter = ('language', 'publisher', 'publication_date')
