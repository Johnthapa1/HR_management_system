# Generated by Django 4.2.2 on 2023-08-17 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0006_alter_employeedesignation_designation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='employee_designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employeedesignation'),
        ),
        migrations.AlterModelTable(
            name='employeedesignation',
            table='designation_name',
        ),
        migrations.DeleteModel(
            name='EmployeeDepartment',
        ),
    ]
