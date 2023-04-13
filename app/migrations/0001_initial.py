# Generated by Django 4.1.7 on 2023-04-13 14:41

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
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=250)),
                ('client_status', models.CharField(choices=[('Potential', 'Potential'), ('Existing', 'Existing')], default='Potential', max_length=16)),
                ('sales_contact', models.ForeignKey(limit_choices_to={'team': 'Sales'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('contract_status', models.CharField(choices=[('New', 'New'), ('Signed', 'Signed')], default='New', max_length=16)),
                ('amount', models.FloatField()),
                ('payment_due', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('sales_contact', models.ForeignKey(limit_choices_to={'team': 'Sales'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('event_status', models.CharField(choices=[('New', 'New'), ('Current', 'Current'), ('Finished', 'Finished')], default='New', max_length=16)),
                ('attendee', models.IntegerField()),
                ('event_date', models.DateTimeField()),
                ('notes', models.TextField()),
                ('contract', models.OneToOneField(limit_choices_to={'contract_status': 'Signed'}, on_delete=django.db.models.deletion.CASCADE, to='app.contract')),
                ('support_contact', models.ForeignKey(limit_choices_to={'team': 'Support'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
