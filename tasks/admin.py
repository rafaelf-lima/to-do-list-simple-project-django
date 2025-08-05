from django.contrib import admin
from tasks.models import Task
# Register your models here.
@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'completed')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')


