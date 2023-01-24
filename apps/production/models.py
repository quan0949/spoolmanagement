import email
from statistics import mode
from tkinter.tix import Tree
from django.db import models

# Create your models here.

class ProductionData(models.Model):
    id = models.IntegerField(primary_key=True)
    issue_date = models.DateField()
    employee_name = models.CharField(max_length=20)
    production_code = models.CharField(max_length=20)
    product_series = models.CharField(max_length=20)
    product_code = models.CharField(max_length=20)
    production_time = models.IntegerField()
    product_quantity = models.IntegerField()
    ng_quantity = models.IntegerField()
    stage = models.CharField(max_length=20)
    basket = models.CharField(max_length=20)
    note = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.production_code

    # JSON
    def get_data(self):
        return {
            'id': self.id,
            'issue_date': self.issue_date,
            'employee_name': self.employee_name,
            'production_code': self.production_code,
            'product_series': self.product_series,
            'product_code': self.product_code,
            'production_time': self.production_time,
            'product_quantity': self.product_quantity,
            'ng_quantity': self.ng_quantity,
            'stage': self.stage,
            'basket': self.basket,
            'note': self.note,
        }

# Use to input the total data plan before production each month 
class ProductionPlan(models.Model):
    id = models.IntegerField(primary_key=True)
    production_code = models.CharField(max_length=20)
    product_code = models.CharField(max_length=20)
    product_quantity = models.IntegerField()
    product_series = models.CharField(max_length=20)
    issue_date = models.DateField()
    end_date = models.DateField()
    day_1 = models.IntegerField()
    day_2 = models.IntegerField()
    day_3 = models.IntegerField()
    day_4 = models.IntegerField()
    day_5 = models.IntegerField()
    day_6 = models.IntegerField()
    day_7 = models.IntegerField()
    day_8 = models.IntegerField()
    day_9 = models.IntegerField()
    day_10 = models.IntegerField()
    day_11 = models.IntegerField()
    day_12 = models.IntegerField()
    day_13 = models.IntegerField()
    day_14 = models.IntegerField()
    day_15 = models.IntegerField()
    day_16 = models.IntegerField()
    day_17 = models.IntegerField()
    day_18 = models.IntegerField()
    day_19 = models.IntegerField()
    day_20 = models.IntegerField()
    day_21 = models.IntegerField()
    day_22 = models.IntegerField()
    day_23 = models.IntegerField()
    day_24 = models.IntegerField()
    day_25 = models.IntegerField()
    day_26 = models.IntegerField()
    day_27 = models.IntegerField()
    day_28 = models.IntegerField()
    day_29 = models.IntegerField()
    day_30 = models.IntegerField()
    day_31 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.production_code