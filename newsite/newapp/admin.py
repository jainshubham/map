from newapp.models import Poll
from django.contrib import admin

from newapp.models import Choice

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]

admin.site.register(Choice)

admin.site.register(Poll, PollAdmin)
