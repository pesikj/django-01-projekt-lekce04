from django.contrib import admin
import crm.models

admin.site.register(crm.models.Company)
admin.site.register(crm.models.Opportunity)
admin.site.register(crm.models.Employee)