from django.contrib import admin

from .models import *

admin.site.register(CommentThread)
admin.site.register(Finding)
admin.site.register(Comment)

# Register your models here.
