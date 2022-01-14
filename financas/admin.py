from django.contrib import admin
from .models import User, Finance

class Users(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_display_links = ['id', 'name']
    list_per_page = 5

class Finances(admin.ModelAdmin):
    list_display = ['id', 'user', 'salary', 'extra_income', 'rent_expenses',
                    'market_expenses', 'extra_expenses', 'receipt_date']
    list_display_links = ['id', 'user']
    search_fields = ['user']
    list_per_page = 5

admin.site.register(User, Users)
admin.site.register(Finance, Finances)

