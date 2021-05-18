from django.contrib import admin
from .models import Category, Task

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','status', 'deadline']

