# Generated by Django 4.2.2 on 2023-11-28 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_deadline', models.DateTimeField()),
                ('assigned_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('assigned_date', models.DateTimeField()),
                ('work_description', models.CharField(max_length=200)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'assign_project',
                'ordering': ['-project_name'],
            },
        ),
    ]
