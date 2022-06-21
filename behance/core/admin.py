from django.contrib import admin
from .models import Work, Tags, Tools_used, Comment
# Register your models here.

admin.site.register(Work)
admin.site.register(Tags)
admin.site.register(Tools_used)
admin.site.register(Comment)