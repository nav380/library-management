from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import PermissionDenied
from .models import User ,userurlpermisson

# Restricting access to the admin page based on superuser status
class AdminUserAdmin(BaseUserAdmin):
    def has_permission(self, request):
        # Allow access only for superusers
        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to access this page.")
        return super().has_permission(request)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Display columns in the user list view
    list_display = ('email', 'username', 'is_staff', 'is_superuser', 'is_customer', 'is_active', 'date_joined')

    # Allow searching by email or username
    search_fields = ('email', 'username')
    ordering = ('email',)

    # Define how the fields are displayed in the user detail form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username',)}),
        ('Role & Permissions', {'fields': ('is_staff', 'is_superuser', 'is_customer')}),
        ('Status', {'fields': ('is_active',)}),  # Remove date_joined from here
    )

    # Define fields for the user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_customer')}
        ),
    )

    # Make `date_joined` read-only for existing users (not editable)
    def get_readonly_fields(self, request, obj=None):
        if obj:  # If it's an existing user, make 'date_joined' readonly
            return self.readonly_fields + ('date_joined',)
        return self.readonly_fields
    
@admin.register(userurlpermisson)
class userurlpermissonAdmin(admin.ModelAdmin):
    list_display = ('user', 'url', 'permission')
    search_fields = ('user__username', 'url')
    list_filter = ('permission',)
    ordering = ('user',)
    fieldsets = (
        (None, {'fields': ('user', 'url', 'permission')}),
    )    
