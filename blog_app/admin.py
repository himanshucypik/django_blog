from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "created_at")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ("post", "user", "text", "is_approved", "created_at")
	list_filter = ("is_approved", "created_at")
	actions = ["approve_comments"]

	def approve_comments(self, request, queryset):
		queryset.update(is_approved=True)
