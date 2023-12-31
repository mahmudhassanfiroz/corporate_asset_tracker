# Generated by Django 4.2.3 on 2023-08-25 15:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('asset_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='device',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checked_in_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='device',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='asset_tracker.device'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkouts', to='asset_tracker.employee'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Enter the phone number of the employee.', max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='device',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='asset_tracker.company'),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='serial_number',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(blank=True, help_text='Enter the address of the employee.', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(help_text='Select the company the employee belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='company', to='asset_tracker.company'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateField(auto_now=True, help_text='The date the employee joined the company.'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(help_text='Enter the email address of the employee.', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(help_text='Enter the first name of the employee.', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(help_text='Enter the last name of the employee.', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Enter the phone number of the employee.', max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_tracker.location'),
        ),
    ]
