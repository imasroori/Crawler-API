from django.contrib import admin

from api.models import Company, CompanyInfo


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'ricCode']


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company']


tables = (Company, CompanyInfo)

for table in tables:
    admin.site.register(table, globals()[f'{table.__name__}Admin'])
