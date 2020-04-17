from django.contrib import admin
from api.models import Company
# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin)
    list_display =('id', 'name')