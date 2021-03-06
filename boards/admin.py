from django.contrib import admin
from .models import Board, Comment


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at', )
    readonly_fields = ['created_at', 'updated_at', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', )
    readonly_fields = ['created_at', ]



