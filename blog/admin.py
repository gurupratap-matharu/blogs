from django.contrib import admin

from blog.models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish", "status")
    list_filter = ("status", "created", "publish", "author")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "post", "created", "active")
    list_filter = ("active", "created", "updated")
    list_editable = ("active",)
    search_fields = ("name", "email", "body")
    date_heirarchy = "created"
    ordering = ("-active", "created")


admin.site.register(Comment, CommentAdmin)
