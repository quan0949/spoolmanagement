from django.contrib import admin
from .models import ProductionData, ProductionPlan

# Register your models here.
class ProductionDataAdmin(admin.ModelAdmin):
    list_display = ['issue_date', 'production_code', 'product_series', 'product_code', 'product_quantity', 'ng_quantity', 'stage', 'employee_name', 'created_at']
    search_fields = ['issue_date', 'production_code', 'product_series', 'product_code', 'stage']
    list_filter = ['production_code', 'product_series' ,'issue_date']
    list_per_page = 12

admin.site.register(ProductionData, ProductionDataAdmin)

class ProductionPlanAdmin(admin.ModelAdmin):
    search_fields = ['production_code', 'product_series', 'product_code']
    list_filter = ['production_code', 'product_series', 'product_code']
    list_per_page = 12

admin.site.register(ProductionPlan, ProductionPlanAdmin)