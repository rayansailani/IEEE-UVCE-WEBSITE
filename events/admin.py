from django.contrib import admin
from .models import Event, Update


# configure the admin page later

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_name', 'date', 'author'
    )
    search_fields = ('event_name', 'date', 'author')


admin.site.register(Event, EventAdmin)


# class GalleryAdmin(admin.ModelAdmin):
#     list_display = ('author',)
#     search_fields = ('author',)


# admin.site.register(Gallery, GalleryAdmin)


class UpdateAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'till_when', 'author'
    )
    search_fields = ('till_when', 'author', 'title')


admin.site.register(Update, UpdateAdmin)
