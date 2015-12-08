from django.contrib import admin

# Register your models here.
from west.models import Character,Contact,Tag

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )
    list_display = ('name','age', 'email') # list
    search_fields = ('name',)

admin.site.register(Contact, ContactAdmin)
admin.site.register([Character, Tag])

# Register your models here.
#admin.site.register([Character, Contact, Tag])