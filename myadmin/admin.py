from django.contrib import admin
from myadmin.models import Notice

# Register your models here.
admin.site.site_header = 'Notice Hub WebApp'
admin.site.index_title = 'Admin Panel'

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id','subject','description','created_at','updated_at']
    search_fields = ['id','subject','created_at','updated_at']

admin.site.register(Notice, NoticeAdmin)
