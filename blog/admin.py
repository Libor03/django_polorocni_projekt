from django.contrib import admin

# Register your models here.

from .models import Animal, Type, Attachment


# Minimal registration of Models.
admin.site.register(Animal)
admin.site.register(Type)

class BlogCommentsInline(admin.TabularInline):
    """
    Used to show 'existing' blog comments inline below associated blogs
    """
    model = Attachment
    max_num=0

class BlogAdmin(admin.ModelAdmin):
    """
    Administration object for Blog models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of blog comments in blog view (inlines)
    """
    list_display = ('name', 'author', 'post_date')
    inlines = [BlogCommentsInline]
