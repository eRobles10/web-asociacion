from django.contrib import admin
from .models import Benefits

# Register your models here.
class BenefitsAdmin(admin.ModelAdmin): 
    readonly_fields = ('created','updated')
    list_display =  ('title','order')


admin.site.register(Benefits, BenefitsAdmin)