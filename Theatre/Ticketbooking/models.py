from django.db import models

from django.contrib import admin

class Ticket(models.Model):
    Ticket_ID=models.IntegerField(primary_key=True)
    Movie_name=models.CharField(max_length=30)
    Ticket_Amt=models.IntegerField()
    cust_no=models.IntegerField()
    cust_name=models.CharField(max_length=30)

class TicketAdmin(admin.ModelAdmin):
    list_display=('Ticket_ID','Movie_name','Ticket_Amt','cust_no','cust_name')