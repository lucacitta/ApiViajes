from django.contrib import admin

from .models import Passanger, Travel

# Register your models here
class TravelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'destination',
        'start_date',
        'end_date'
    )

class PassangerAdmin(admin.ModelAdmin):
    list_display = (
        'type_of_document',
        'document_id',
    )


admin.site.register(Passanger, PassangerAdmin)
admin.site.register(Travel, TravelAdmin)
