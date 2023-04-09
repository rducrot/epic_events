from django.contrib import admin

from app.models import Client, Contract, Event


class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'company_name', 'sales_contact')
    ordering = ('sales_contact',)
    list_filter = ('sales_contact',)
    search_fields = ('last_name', 'first_name', 'email', 'company_name')


class ContractAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client', 'status', 'amount', 'payment_due', 'sales_contact')
    list_filter = ('sales_contact',)
    search_fields = ('client', 'sales_contact')


class EventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client', 'attendee', 'event_date', 'support_contact')
    list_filter = ('support_contact',)
    search_fields = ('client', 'support_contact')


admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
