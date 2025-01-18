from django.contrib import admin
from .models import Folder, Files


class FilesInline(admin.TabularInline):
    model = Files
    extra = 1  # Number of empty forms to display in the admin


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = ('uid', 'created_at', 'uploaded_at')
    search_fields = ('uid',)  # Allows searching by 'uid'
    inlines = [FilesInline]  # Displays the inline form for related files


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = ('file', 'folder', 'created_at', 'uploaded_at')
    search_fields = ('file',)  # Allows searching by 'file'
    list_filter = ('folder',)  # Allows filtering by 'folder'
