from django.contrib import admin

# Register your models here.
from .models import JMIR

#admin
#pass123



class JMIRAdmin(admin.ModelAdmin):
	list_display = ("pk", "reference_count", "publisher", 'DOI', "volume", "title", "issn", "url")

admin.site.register(JMIR, JMIRAdmin)