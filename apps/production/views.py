from email import message
import imp
from django.contrib import messages
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from apps.production.models import ProductionData, ProductionPlan
from django.db.utils import DatabaseError,IntegrityError
from django.shortcuts import get_object_or_404
from django.db.models import Sum
# Create your views here.

@login_required
def inputdata(request):
    if request.method == 'POST':
       if request.POST.get('issue_date') \
           and request.POST.get('employee_name') \
           and request.POST.get('production_code') \
           and request.POST.get('product_code') \
           and request.POST.get('stage') \
           and request.POST.get('basket') \
           and request.POST.get('note'):
                production = ProductionData()
                production.issue_date = request.POST.get('issue_date')
                production.employee_name = request.POST.get('employee_name')
                production.production_code = request.POST.get('production_code')
                str = request.POST.get('product_code')
                production.product_series = str[:6]
                production.product_code = request.POST.get('product_code')
                production.production_time = request.POST.get('production_time')
                production.product_quantity = request.POST.get('product_quantity')
                production.ng_quantity = request.POST.get('ng_quantity')
                production.stage = request.POST.get('stage')
                production.basket = request.POST.get('basket')
                production.note = request.POST.get('note')
                production.save()
                data_list = ProductionData.objects.all().order_by('-created_at')
                messages.success(request, "Add data successfully")
                return HttpResponseRedirect('/inputdata/')
    else:
        data_list = ProductionData.objects.all().order_by('-created_at')
        context  = {
            'production_data': data_list,
        }
        return render(request, '3. production/inputdata.html', context)

# Function to View Production data individally
def production(request, production_id):
    production = ProductionData.objects.get(id = production_id)
    if production != None:
        return render(request, '3. production/edit_inputdata.html', {'production': production})

# Function to Edit Production data
def edit_production_data(request, production_id):
    if request.method == 'POST':
        production = ProductionData.objects.get(id = production_id)
        if production != None:
            production.issue_date = request.POST.get('issue_date')
            production.employee_name = request.POST.get('employee_name')
            production.production_code = request.POST.get('production_code')
            production.product_code = request.POST.get('product_code')
            production.production_time = request.POST.get('production_time')
            production.product_quantity = request.POST.get('product_quantity')
            production.ng_quantity = request.POST.get('ng_quantity')
            production.stage = request.POST.get('stage')
            production.basket = request.POST.get('basket')
            production.note = request.POST.get('note')
            production.save()
            messages.success(request, "Updated data successfully")
            production_data_list = ProductionData.objects.all().order_by('-created_at')
            return HttpResponseRedirect('/inputdata/')
        else:
            data_list = ProductionData.objects.all().order_by('-created_at')
            return render(request, '3. production/inputdata.html', {"production_data":data_list})

# Function to Delete Production data
def delete_production_data(request, production_id):
    production = ProductionData.objects.get(id = production_id)
    production.delete()
    messages.success(request, "Delete data successfully")
    data_list = ProductionData.objects.all().order_by('-created_at')
    return HttpResponseRedirect('/inputdata/')

@login_required
def plan(request):
    if request.method == 'POST':
       if request.POST.get('production_code') \
           and request.POST.get('product_code') \
           and request.POST.get('product_quantity') \
           and request.POST.get('issue_date') \
           and request.POST.get('end_date'):
                production = ProductionPlan()
                production.production_code = request.POST.get('production_code')
                production.product_code = request.POST.get('product_code')
                production.product_quantity = request.POST.get('product_quantity')
                str = request.POST.get('product_code')
                production.product_series = str[:6]
                production.issue_date = request.POST.get('issue_date')
                production.end_date = request.POST.get('end_date')
                production.day_1 = 0
                production.day_2 = 0
                production.day_3 = 0
                production.day_4 = 0
                production.day_5 = 0
                production.day_6 = 0
                production.day_7 = 0
                production.day_8 = 0
                production.day_9 = 0
                production.day_10 = 0
                production.day_11 = 0
                production.day_12 = 0
                production.day_13 = 0
                production.day_14 = 0
                production.day_15 = 0
                production.day_16 = 0
                production.day_17 = 0
                production.day_18 = 0
                production.day_19 = 0
                production.day_20 = 0
                production.day_21= 0
                production.day_22= 0
                production.day_23= 0
                production.day_24= 0
                production.day_25= 0
                production.day_26= 0
                production.day_27= 0
                production.day_28= 0
                production.day_29= 0
                production.day_30= 0
                production.day_31= 0
                production.save()

                return HttpResponseRedirect('/plan/')
    else:
        plan_list = ProductionPlan.objects.all().order_by('id')
        context  = {
            'production_plan': plan_list,
        }
        return render(request, '3. production/plan.html', context)

# Function to View Production Plan individally
def view_plan(request, production_id):
    view_plan = ProductionPlan.objects.get(id = production_id)
    if view_plan != None:
        return render(request, '3. production/edit_plan.html', {'view_plan': view_plan})

# Function to Edit Production Plan
def edit_production_plan(request, production_id):
    if request.method == 'POST':
        production = ProductionPlan.objects.get(id = production_id)
        if production != None:
            production.production_code = request.POST.get('production_code')
            production.product_code = request.POST.get('product_code')
            production.product_quantity = request.POST.get('product_quantity')
            production.product_series = request.POST.get('product_series')
            production.issue_date = request.POST.get('issue_date')
            production.end_date = request.POST.get('end_date')
            production.day_1 = request.POST.get('day_1')
            production.day_2 = request.POST.get('day_2')
            production.day_3 = request.POST.get('day_3')
            production.day_4 = request.POST.get('day_4')
            production.day_5 = request.POST.get('day_5')
            production.day_6 = request.POST.get('day_6')
            production.day_7 = request.POST.get('day_7')
            production.day_8 = request.POST.get('day_8')
            production.day_9 = request.POST.get('day_9')
            production.day_10 = request.POST.get('day_10')
            production.day_11 = request.POST.get('day_11')
            production.day_12 = request.POST.get('day_12')
            production.day_13 = request.POST.get('day_13')
            production.day_14 = request.POST.get('day_14')
            production.day_15 = request.POST.get('day_15')
            production.day_16 = request.POST.get('day_16')
            production.day_17 = request.POST.get('day_17')
            production.day_18 = request.POST.get('day_18')
            production.day_19 = request.POST.get('day_19')
            production.day_20 = request.POST.get('day_20')
            production.day_21= request.POST.get('day_21')
            production.day_22= request.POST.get('day_22')
            production.day_23= request.POST.get('day_23')
            production.day_24= request.POST.get('day_24')
            production.day_25= request.POST.get('day_25')
            production.day_26= request.POST.get('day_26')
            production.day_27= request.POST.get('day_27')
            production.day_28= request.POST.get('day_28')
            production.day_29= request.POST.get('day_29')
            production.day_30= request.POST.get('day_30')
            production.day_31= request.POST.get('day_31')
            production.save() 
            return HttpResponseRedirect('/plan/')
        else:
            plan_list = ProductionPlan.objects.all().order_by('id')
            context  = {
                'production_plan': plan_list,
            }
            return render(request, '3. production/plan.html', context)

@login_required
def data(request):
    total_data_list = ProductionData.objects.filter().values('issue_date').order_by('issue_date').annotate(sum=Sum('product_quantity'))
    sy3000_data_list = ProductionData.objects.filter(product_series="SY3000").values('issue_date').order_by('issue_date').annotate(sum=Sum('product_quantity'))
    sy5000_data_list = ProductionData.objects.filter(product_series="SY5000").values('issue_date').order_by('issue_date').annotate(sum=Sum('product_quantity'))
    sy7000_data_list = ProductionData.objects.filter(product_series="SY7000").values('issue_date').order_by('issue_date').annotate(sum=Sum('product_quantity'))
    sy9000_data_list = ProductionData.objects.filter(product_series="SY9000").values('issue_date').order_by('issue_date').annotate(sum=Sum('product_quantity'))
    context  = {
        'total_data_list': total_data_list,
        'sy3000_data_list': sy3000_data_list,
        'sy5000_data_list': sy5000_data_list,
        'sy7000_data_list': sy7000_data_list,
        'sy9000_data_list': sy9000_data_list,
    }
    return render(request, '3. production/data.html', context)

@login_required
def nglist(request):
    return render(request, '3. production/nglist.html')

# JSON
def employee_json(request):
    employees = ProductionData.objects.all()
    data = [employee.get_data() for employee in employees]
    response = {'data': data}
    return JsonResponse(response)

def production_code_json(request, *args, **kwargs):
    production_code_input = kwargs.get('inputData','default')
    product_code = list(ProductionPlan.objects.filter(production_code=production_code_input).values())
    #product_code = ProductionData.objects.all()
    response = {'data': product_code}
    return JsonResponse(response)

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