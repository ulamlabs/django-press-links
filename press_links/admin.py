from django.contrib import admin
from press_links.models import Entry

class EntryAdmin(admin.ModelAdmin):
    model = Entry
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)
    list_display = ('title', 'pub_date', 'status',)
    list_filter = ('site', 'status',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'excerpt',)

admin.site.register(Entry, EntryAdmin)

