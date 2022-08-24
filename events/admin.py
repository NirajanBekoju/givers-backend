from django.contrib import admin
from .models import Events, LikeEvent

# Register your models here.
class LikeEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event', 'date')
    search_fields = ('user', 'event')
    list_per_page = 30

class EventModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'completed')
    list_display_links = ('id', 'name', 'user')
    list_editable = ('completed', )
    list_per_page = 30

admin.site.register(Events, EventModel)
admin.site.register(LikeEvent, LikeEventAdmin)