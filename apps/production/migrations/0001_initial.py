# Generated by Django 4.1.5 on 2023-01-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField()),
                ('employee_name', models.CharField(max_length=20)),
                ('production_code', models.CharField(max_length=20)),
                ('product_series', models.CharField(max_length=20)),
                ('product_code', models.CharField(max_length=20)),
                ('production_time', models.IntegerField()),
                ('product_quantity', models.IntegerField()),
                ('ng_quantity', models.IntegerField()),
                ('stage', models.CharField(max_length=20)),
                ('basket', models.CharField(max_length=20)),
                ('note', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionPlan',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('production_code', models.CharField(max_length=20)),
                ('product_code', models.CharField(max_length=20)),
                ('product_quantity', models.IntegerField()),
                ('product_series', models.CharField(max_length=20)),
                ('issue_date', models.DateField()),
                ('end_date', models.DateField()),
                ('day_1', models.IntegerField()),
                ('day_2', models.IntegerField()),
                ('day_3', models.IntegerField()),
                ('day_4', models.IntegerField()),
                ('day_5', models.IntegerField()),
                ('day_6', models.IntegerField()),
                ('day_7', models.IntegerField()),
                ('day_8', models.IntegerField()),
                ('day_9', models.IntegerField()),
                ('day_10', models.IntegerField()),
                ('day_11', models.IntegerField()),
                ('day_12', models.IntegerField()),
                ('day_13', models.IntegerField()),
                ('day_14', models.IntegerField()),
                ('day_15', models.IntegerField()),
                ('day_16', models.IntegerField()),
                ('day_17', models.IntegerField()),
                ('day_18', models.IntegerField()),
                ('day_19', models.IntegerField()),
                ('day_20', models.IntegerField()),
                ('day_21', models.IntegerField()),
                ('day_22', models.IntegerField()),
                ('day_23', models.IntegerField()),
                ('day_24', models.IntegerField()),
                ('day_25', models.IntegerField()),
                ('day_26', models.IntegerField()),
                ('day_27', models.IntegerField()),
                ('day_28', models.IntegerField()),
                ('day_29', models.IntegerField()),
                ('day_30', models.IntegerField()),
                ('day_31', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]