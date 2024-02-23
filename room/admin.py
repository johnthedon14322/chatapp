from django.contrib import admin

# Register your models here.

from room.models import Messages

admin.site.register(Messages)
