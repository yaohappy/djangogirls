from django.contrib import admin
from trips.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'location')
	search_fields = ('title', 'location')

admin.site.register(Post, PostAdmin)


