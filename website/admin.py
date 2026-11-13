from django.contrib import admin
from website.models import Contact



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('id', 'name', 'email', 'subject', 'created_date')
    search_fields = ('name', 'email', 'message')
    list_filter = ('name', 'email','created_date')



    