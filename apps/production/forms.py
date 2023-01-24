from .models import ProductionData
from django import forms
import datetime
 
class ProductionDataForm(forms.ModelForm):
    ## change the widget of the date field.
    dob = forms.DateField(
        label='What is your birth date?', 
        # change the range of the years from 1980 to currentYear - 5
        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year-5))
    )
     
    def __init__(self, *args, **kwargs):
        super(ProductionDataForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
 
    class Meta:
        model = ProductionData
        fields = ("__all__")

                # index = 1
                # for data in data_list:
                #     old_data = ProductionData.objects.get(id=data.id)
                #     data.id = index
                #     data.save()
                #     old_data.delete()
                #     index = index + 1

# try:
#   #write code to execute query here
# except IntegrityError:
#    #write code to handle exception here(example creating a log)

# def add_employee(request):
#     if request.method=="POST":
#         if request.POST.get('name') and \
#             request.POST.get('email') and \
#             request.POST.get('occupation') and \
#             request.POST.get('salary') and \
#             request.POST.get('gender') \
#             or request.POST.get('note'):
#             employee = Employee()
#             employee.name = request.POST.get('name')
#             employee.email = request.POST.get('email')
#             employee.occupation = request.POST.get('occupation')
#             employee.salary = request.POST.get('salary')
#             employee.gender = request.POST.get('gender')
#             employee.note = request.POST.get('note')
#             employee.save()
#             messages.success(request, "Employee added successfully !")
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, 'includes/add.html')

# # Function to View employee data invidually
# def employee(request, employee_id):
#     employee = Employee.objects.get(id=employee_id)
#     if employee != None:
#         return render(request, "includes/edit.html", {'employee':employee})

# # Function to Edit Employee
# def edit_employee(request):
#     if request.method=="POST":
#         employee = Employee.objects.get(id = request.POST.get('id'))
#         if employee != None:
#             employee = Employee()
#             employee.name = request.POST.get('name')
#             employee.email = request.POST.get('email')
#             employee.occupation = request.POST.get('occupation')
#             employee.salary = request.POST.get('salary')
#             employee.gender = request.POST.get('gender')
#             employee.note = request.POST.get('note')
#             employee.save()
#             messages.success(request, "Employee Updated successfully !")
#             return HttpResponseRedirect("/")

# # Function to Delete Employee
# def delete_employee(request, employee_id):
#     employee = Employee.objects.get(id = employee_id)
#     employee.delete()
#     messages.success(request, "Employee Deleted successfully !")
#     return HttpResponseRedirect("/")

# # ajax_posting function
# def add_data(request):
#    if request.method == 'POST':
#        if request.POST.get('issue_date') \
#            and request.POST.get('employee_name') \
#            and request.POST.get('production_code') \
#            and request.POST.get('product_code') \
#            and request.POST.get('stage') \
#            and request.POST.get('basket') \
#            and request.POST.get('note'):
#                 production_data = ProductionData()
#                 production_data.issue_date = request.POST.get('issue_date')
#                 production_data.employee_name = request.POST.get('employee_name')
#                 production_data.production_code = request.POST.get('production_code')
#                 production_data.product_code = request.POST.get('product_code')
#                 production_data.production_time = request.POST.get('production_time')
#                 production_data.product_quantity = request.POST.get('product_quantity')
#                 production_data.ng_quantity = request.POST.get('ng_quantity')
#                 production_data.stage = request.POST.get('stage')
#                 production_data.basket = request.POST.get('basket')
#                 production_data.note = request.POST.get('note')
#                 production_data.save()
#                 messages.success(request, "Add data successfully")
#                 return HttpResponseRedirect("/")
#        else:
#             messages.success(request, "Wrong")
#    else:
#         data_list = ProductionData.objects.all()
#         return render(request, '3. production/inputdata.html', {"production_data":data_list})