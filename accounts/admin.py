# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['email', 'username', 'first_name', 'last_name', 'signup_time', 'is_staff']
#     list_filter = ['is_staff', 'is_active', 'signup_time']
#     fieldsets = UserAdmin.fieldsets + (
#         ('Additional Info', {'fields': ('signup_time', 'last_login_time', 'otp', 'otp_created_at')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ('Additional Info', {'fields': ('email', 'first_name', 'last_name')}),
#     )
#     readonly_fields = ['signup_time', 'last_login_time', 'otp_created_at']

# admin.site.register(CustomUser, CustomUserAdmin)