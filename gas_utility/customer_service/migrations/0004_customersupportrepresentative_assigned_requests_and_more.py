# Generated by Django 5.1.7 on 2025-03-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0003_alter_customer_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersupportrepresentative',
            name='assigned_requests',
            field=models.ManyToManyField(blank=True, related_name='assigned_representatives', to='customer_service.servicerequest'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(db_index=True, max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='customersupportrepresentative',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customersupportrepresentative',
            name='phone',
            field=models.CharField(db_index=True, max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed')], db_index=True, default='pending', max_length=20),
        ),
    ]
