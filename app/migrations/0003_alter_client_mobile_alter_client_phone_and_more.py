# Generated by Django 4.1.7 on 2023-04-26 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_client_sales_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='mobile',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(blank=True, limit_choices_to={'team': 'Sales'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='app.client'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='sales_contact',
            field=models.ForeignKey(blank=True, limit_choices_to={'team': 'Sales'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='contract',
            field=models.OneToOneField(limit_choices_to={'contract_status': 'Signed', 'event': None}, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='app.contract'),
        ),
        migrations.AlterField(
            model_name='event',
            name='support_contact',
            field=models.ForeignKey(blank=True, limit_choices_to={'team': 'Support'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
