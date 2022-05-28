from django.contrib import admin
from .models import Csat_filtred_phones

class CreatedAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Csat_filtred_phones, CreatedAdmin)
