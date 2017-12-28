from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Dictionary

# # Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class PortfolioInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'portfolio'
#
#
# # Define a new User admin
# class UserAdmin(UserAdmin):
#     inlines = (PortfolioInline, )
#
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


class DictionaryAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = ['word']
    list_display = ['word', 'description']


admin.site.register(Dictionary, DictionaryAdmin)
