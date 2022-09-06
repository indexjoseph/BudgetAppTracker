from django.contrib import admin
from budget_app.models import Transaction, Entry

admin.site.register(Transaction) # Register the Transaction model to the Django adminstration site
admin.site.register(Entry) # Register the Entry model to the Django adminstration site
# Register your models here.
