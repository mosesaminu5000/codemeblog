from django.contrib import admin

from .models import post, Category, comments

class CommentItemInline(admin.TabulerInline):
    model = comment
    row_id_fields = ['post']

class postAdmin(admin.ModelAdmin):
    search_fields = ['tittle', 'intro', 'body']
    list_display = ['tittle', 'slug', 'category', 'created_at' ]
    list_filter = ['category', 'created_at']
    inlines = ['CommentItemInline']
    prepopulated_fields = {'slug': ('tittle',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['tittle']
    list_display = ['tittle']
    prepopulated_fields = {'slug': ('tittle',)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display =['name', 'post', 'created_at']      

admin.site.register(post, postAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(comments,CommentAdmin)