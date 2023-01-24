from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('inputdata/', views.inputdata, name='production-inputdata'),
    path('plan/', views.plan, name='production-plan'),
    path('data/', views.data, name='production-data'),
    path('nglist/', views.inputdata, name='production-nglist'),
    
    # Path to View Production data individually
    path('production/<str:production_id>', views.production, name="production"),
    # Path to Edit Production data
    path('edit_production_data/<str:production_id>', views.edit_production_data, name="edit_production_data"),
    # Path to Delete Production data
    path('delete_production_data/<str:production_id>', views.delete_production_data, name="delete_production_data"),

    # Path to View Production Plan individually
    path('view_plan/<str:production_id>', views.view_plan, name="view_plan"),
    # Path to Edit Production Plan
    path('edit_production_plan/<str:production_id>', views.edit_production_plan, name="edit_production_plan"),

    # JSON Response
    path('json/', views.employee_json, name = 'employee-json'),
    path('production-code-json/<str:inputData>/', views.production_code_json, name = 'production-code-json'),
]
