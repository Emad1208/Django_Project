from django.contrib import admin

from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('id', 'title', 'counted_views', 'status', 'published_date', 'created_date')
    # fields = ('title', 'counted_views', 'status')
    search_fields = ('title', 'content')
    list_filter = ('status','created_date',)




# admin.site.register(Post,PostAdmin)