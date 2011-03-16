
from dblog.models import Blog
from dblog.models import Comment
from django.contrib import admin


class CommentInline(admin.TabularInline):
   model = Comment
   extra = 1

class BlogAdmin(admin.ModelAdmin):
     fieldsets = [
        (None,               {'fields': ['title']}),
        ('None', {'fields': ['post_date']}),
	('None', {'fields': ['reply_to']}),
	('Comments', {'fields': ['content']}),
   	 ]
    # inlines = [CommentInline]
    # list_display = ('title', 'post_date', 'reply_to')
    # list_filter = ['post_date']
    # search_fields = ['title']
    # date_hierarchy = 'post_date'
admin.site.register(Blog,BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
     fieldsets = [
	(None,               {'fields': ['in_reference_to']}),
        (None,               {'fields': ['content']}),
        ('Rating', {'fields': ['rating']}),
   	 ]

admin.site.register(Comment,CommentAdmin)
