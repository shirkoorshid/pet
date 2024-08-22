# admin.py
from django.contrib import admin
from .models import Pet
from .models import ContactSubmission

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'temperament',	'description' , 'medical_history')



admin.site.register(ContactSubmission)  