from django.contrib import admin
from .models import Room, Message

# Register your models here.
admin.site.register(Room)


@admin.register(Message)
class MessageClass(admin.ModelAdmin):
    list_filter = ("room", )
    list_display = ("value", )
